def count_words(text):
    words = text.lower().split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

# проверка
print(count_words("кот сидит на окне кот смотрит в окно"))