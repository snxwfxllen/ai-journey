from day2 import count_words

# 1. Читаем файл
with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Считаем слова (используем функцию из day2)
freq = count_words(text)

# 3. Сортируем по частоте (по убыванию) и берём топ-10
# freq.items() превращает словарь в список пар: [('кот', 3), ('собака', 2), ...]
# key=lambda x: x[1] говорит: "сортируй по второму элементу пары (то есть по числу)"
# reverse=True означает "по убыванию" (от большего к меньшему)
top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

# 4. Записываем в top.txt
with open('top.txt', 'w', encoding='utf-8') as f:
    for word, count in top10:
        f.write(f'{word}: {count}\n')

print("Готово! Смотри top.txt")