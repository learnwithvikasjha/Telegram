from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    try:
        print(request.json)
        print(request.json["message"]["text"])
        question = request.json["message"]["text"]
        print("calling function to get answer")
        answer = get_answer(question)
        print("calling reply to chat function")
        status = reply_to_chat(request.json, answer)
    except:
        print("Error")
    
    return {"status": "Success"}

def get_answer(question):     
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
    print("returning the answer from chatgpt")
    return response.json()["choices"][0]["message"]["content"]

def reply_to_chat(json, answer):
    try:
        TOKEN = "1239352810:AAEWOq98yYsylhbTz9nZNmLa6uXW-W4rE6w"
        chat_id = json["message"]["chat"]["id"]
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={answer}"
        print(url)
        resp = requests.get(url)
        print(resp)
        return resp
    except Exception as e:
        print(e)
        return "Failed to reply on telegram"

if __name__ == '__main__':
    app.run()
