import requests
import json

def chat_with_ollama(prompt: str):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "gemma3:1b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
        }
    }

    print("💬 AI 回應：", end="", flush=True)
    
    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode('utf-8'))
                    
                    # 檢查是否有訊息內容
                    if 'message' in chunk and 'content' in chunk['message']:
                        content = chunk['message']['content']
                        print(content, end="", flush=True)
                    
                    # 檢查是否完成
                    if chunk.get('done', False):
                        print()  # 換行
                        break
                        
                except json.JSONDecodeError:
                    continue
                    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ 請求錯誤: {e}")
    except Exception as e:
        print(f"\n❌ 處理錯誤: {e}")

def chat_loop():
    print("歡迎使用本地端 LLM 聊天機器人（輸入 q 離開）")
    while True:
        user_input = input("👤 你說：")
        if user_input.lower() == 'q':
            break
        chat_with_ollama(user_input)
        print()  # 空行分隔

chat_loop()