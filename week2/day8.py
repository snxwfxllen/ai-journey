import sqlite3

# 1. Подключаемся к базе данных. 
# Если файла 'astra_memory.db' нет, Python создаст его автоматически.
conn = sqlite3.connect('astra_memory.db')

# 2. Создаем "курсор" — это объект, через который мы отправляем SQL-команды в базу.
cursor = conn.cursor()

# 3. Создаем таблицу (если её еще нет).
# Мы будем хранить: ID записи, кто говорит (role), текст (content) и время (timestamp).
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# 4. Сохраняем изменения (коммитим) и закрываем соединение
conn.commit()
conn.close()

print("Успех! База данных astra_memory.db создана, таблица messages готова.")