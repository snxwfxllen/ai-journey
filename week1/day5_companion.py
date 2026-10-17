from day5 import ask_ollama

class Companion:
    def __init__(self, name, mood="нейтральное"):
        self.name = name
        self.mood = mood
        # Вот здесь мы задаем её личность и пол
        self.persona = (
            f"Ты — {self.name}, ИИ-компаньон. Ты ДЕВУШКА. "
            "Ты обязана говорить о себе только в женском роде (например: 'я подумала', 'я рада', 'я сделала'). "
            "Ты общаешься живо, дружелюбно и естественно."
        )

    def talk(self, message):
        # Собираем промпт: Личность + Настроение + Сообщение пользователя
        prompt = (
            f"Системная инструкция: {self.persona}\n"
            f"Твое текущее настроение: {self.mood}.\n"
            f"Пользователь говорит: {message}\n"
            f"Твой ответ:"
        )
        
        print(f"[{self.name} печатает...]")
        reply = ask_ollama(prompt)
        
        return f"[{self.name}, настроение: {self.mood}]: {reply}"

if __name__ == "__main__":
    my_ai = Companion("Астра", mood="радостное")
    
    print(f"--- Чат с {my_ai.name} ---")
    print("Напиши 'выход', чтобы закончить разговор.\n")
    
    while True:  # Бесконечный цикл
        user_input = input("Ты: ")  # Ждем, пока ты что-то напишешь
        
        if user_input.lower() in ["выход", "exit", "quit"]:
            print(f"{my_ai.name}: Пока! Было классно пообщаться.")
            break  # Выходим из цикла
            
        # Если не выход, отправляем запрос ИИ
        response = my_ai.talk(user_input)
        print(response + "\n")