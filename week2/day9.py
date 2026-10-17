import sqlite3

# 1. Функция для сохранения сообщения
def save_message(role, content):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    
    # Команда INSERT INTO добавляет новую строку в таблицу.
    # Знаки вопроса (?, ?) — это защита от взлома (SQL-инъекций). 
    # Мы передаем данные вторым аргументом в кортеже.
    cursor.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)", 
        (role, content)
    )
    
    conn.commit()
    conn.close()
    print(f"В память записано: [{role}] {content}")

# 2. Функция для чтения последних сообщений (пригодится завтра)
def get_recent_messages(limit=5):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    
    # SELECT берет данные, ORDER BY id DESC сортирует от новых к старым.
    # LIMIT ограничивает количество.
    cursor.execute(
        "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", 
        (limit,)
    )
    
    # fetchall() забирает все найденные строки
    rows = cursor.fetchall()
    conn.close()
    
    # Возвращаем в обратном порядке (чтобы старые были первыми)
    return rows[::-1]

# 3. Проверяем, как это работает
if __name__ == "__main__":
    print("--- Тест базы данных ---")
    
    # Сохраняем пару сообщений
    save_message("user", "Привет, Астра!")
    save_message("astra", "Привет! Я рада тебя видеть.")
    
    print("\n--- Читаем из памяти ---")
    history = get_recent_messages(limit=5)
    
    for role, content in history:
        print(f"{role}: {content}")