from flask import Flask, jsonify
import docker
from mongoengine import connect
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Підключення до MongoDB
connect(host="mongodb://mongo:27017/mydb")

# Конфігурація OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Функція для взаємодії з ChatGPT
def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

@app.route('/test', methods=['GET'])
def test():
    client = docker.from_env()
    containers = client.containers.list()
    containers_list = [{"name": container.name, "status": container.status} for container in containers]

    # Додавання перевірки ChatGPT
    gpt_response = chat_with_gpt("Hello, world!")

    return jsonify({"containers": containers_list, "db_status": "connected", "gpt_test": gpt_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
