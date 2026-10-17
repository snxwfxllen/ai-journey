import requests

def ask_ollama(prompt, model_name="qwen3:8b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    # ВОТ ОНА, ЗАЩИТА: мы говорим Python "ПОПРОБУЙ (try) это сделать"
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()['response']
        else:
            return "Ошибка на стороне Ollama."
            
    # А ЕСЛИ НЕ ПОЛУЧИТСЯ (например, Ollama выключена) — сделай ЭТО (except)
    except requests.exceptions.ConnectionError:
        return "[Система]: Ой! Кажется, Ollama не запущена. Проверь значок в трее."