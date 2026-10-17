import requests
import json

def ask_ollama(prompt, model_name="qwen3:8b"):
    # Адрес локального API Ollama
    url = "http://localhost:11434/api/generate"
    
    # Данные, которые мы отправляем
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False  # False означает, что мы ждем весь ответ целиком, а не по кусочкам
    }
    
    # Отправляем POST-запрос
    response = requests.post(url, json=payload)
    
    # Проверяем, что сервер ответил успешно (код 200)
    if response.status_code == 200:
        data = response.json()
        return data['response']
    else:
        return f"Ошибка: {response.status_code}"

# Проверка
if __name__ == "__main__":
    print("Отправляю запрос нейросети...")
    answer = ask_ollama("Привет! Расскажи в двух предложениях, кто ты.")
    print("\nОтвет от ИИ:")
    print(answer)