class Companion:
    def __init__(self, name, mood="нейтральное"):
        # __init__ — это конструктор, вызывается при создании объекта
        self.name = name      # имя компаньона
        self.mood = mood      # настроение

    def say(self, text):
        # метод say возвращает строку с именем, настроением и текстом
        return f"[{self.name}, настроение: {self.mood}] {text}"

    def change_mood(self, new_mood):
        # метод меняет настроение
        self.mood = new_mood
        return f"{self.name} теперь {self.mood}"

# Проверка
if __name__ == "__main__":
    comp = Companion("Астра")
    print(comp.say("Привет, я твой компаньон."))
    print(comp.change_mood("радостное"))
    print(comp.say("Как дела?"))