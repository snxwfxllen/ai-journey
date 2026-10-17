import sqlite3

# Функция инициализации базы (создает таблицу, если ее нет)
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

# ВАЖНО: Вызываем инициализацию сразу при импорте файла
init_db()

def save_message(role, content):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_recent_messages(limit=6):
    conn = sqlite3.connect('astra_memory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows[::-1]