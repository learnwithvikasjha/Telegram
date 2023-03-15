import requests

def auto_answer_chatgpt(question):
        
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

question = input("Please enter any question")
answer = auto_answer_chatgpt(question)
print(answer)


