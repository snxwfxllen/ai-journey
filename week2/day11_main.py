# Мы ИМПОРТИРУЕМ (import) функции из наших новых файлов
from brain import ask_ollama
from memory import save_message, get_recent_messages

class Companion:
    def __init__(self, name, mood="нейтральное"):
        self.name = name
        self.mood = mood
        self.persona = (
            f"Ты — {self.name}, ИИ-компаньон. Ты ДЕВУШКА. "
            "Говори о себе только в женском роде. Ты общаешься живо и дружелюбно."
        )

    def talk(self, user_message):
        save_message("user", user_message)
        history = get_recent_messages(limit=6)
        
        history_text = ""
        for role, content in history:
            speaker = "Пользователь" if role == "user" else self.name
            history_text += f"{speaker}: {content}\n"
            
        prompt = (
            f"Системная инструкция: {self.persona}\n"
            f"Твое текущее настроение: {self.mood}.\n\n"
            f"История вашего диалога:\n{history_text}\n"
            f"{self.name}:"
        )
        
        print(f"[{self.name} печатает...]")
        reply = ask_ollama(prompt)
        
        save_message("astra", reply)
        return f"[{self.name}]: {reply}"

if __name__ == "__main__":
    my_ai = Companion("Астра", mood="радостное")
    print(f"--- Чат с {my_ai.name} ---")
    
    while True:
        user_input = input("Ты: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            break
        print(my_ai.talk(user_input) + "\n")