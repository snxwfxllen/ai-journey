import requests
import sqlite3

# --- 0. ИНИЦИАЛИЗАЦИЯ БАЗЫ (чтобы не было ошибок) ---
def init_db():
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Вызываем её сразу при старте
init_db()

# --- 1. ФУНКЦИЯ ДЛЯ OLLAMA ---
def ask_ollama(prompt, model_name="qwen3:8b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()['response']
    except requests.exceptions.ConnectionError:
        return "Ошибка: Ollama не запущена. Проверь значок в трее."
    return "Ошибка при запросе к ИИ."

# --- 2. ФУНКЦИИ БАЗЫ ДАННЫХ ---
def save_message(role, content):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_recent_messages(limit=6):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    # Берем последние N сообщений (сортируем по убыванию ID)
    cursor.execute("SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    # Возвращаем в правильном хронологическом порядке
    return rows[::-1]

# --- 3. КЛАСС КОМПАНЬОНА ---
class Companion:
    def __init__(self, name, mood="нейтральное"):
        self.name = name
        self.mood = mood
        self.persona = (
            f"Ты — {self.name}, ИИ-компаньон. Ты ДЕВУШКА. "
            "Говори о себе только в женском роде ('я подумала', 'я рада'). "
            "Ты общаешься живо, дружелюбно и естественно. Ты любишь играть в игры и слушать музыку."
        )

    def talk(self, user_message):
        # 1. Сохраняем сообщение пользователя в базу
        save_message("user", user_message)
        
        # 2. Достаем последние 6 сообщений из базы (для контекста)
        history = get_recent_messages(limit=6)
        
        # 3. Формируем историю в виде текста
        history_text = ""
        for role, content in history:
            speaker = "Пользователь" if role == "user" else self.name
            history_text += f"{speaker}: {content}\n"
            
        # 4. Собираем финальный промпт
        prompt = (
            f"Системная инструкция: {self.persona}\n"
            f"Твое текущее настроение: {self.mood}.\n\n"
            f"История вашего диалога:\n{history_text}\n"
            f"{self.name}:"
        )
        
        print(f"[{self.name} печатает...]")
        # 5. Отправляем запрос ИИ
        reply = ask_ollama(prompt)
        
        # 6. Сохраняем ответ Астры в базу
        save_message("astra", reply)
        
        return f"[{self.name}, настроение: {self.mood}]: {reply}"

# --- 4. ЗАПУСК ---
if __name__ == "__main__":
    my_ai = Companion("Астра", mood="радостное")
    
    print(f"--- Чат с {my_ai.name} ---")
    print("Напиши 'выход', чтобы закончить разговор.\n")
    
    while True:
        user_input = input("Ты: ")
        
        if user_input.lower() in ["выход", "exit", "quit"]:
            print(f"{my_ai.name}: Пока! Было классно пообщаться.")
            break
            
        response = my_ai.talk(user_input)
        print(response + "\n")