from flask import Flask, request, jsonify
from flask_cors import CORS  # Необходимо установить пакет Flask-CORS
import json
import os
import logging

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
CORS(app)  # Разрешить все CORS-запросы

@app.route('/store_response', methods=['POST'])
def store_response():
    response = request.get_json()
    message = response.get('message')

    # Выводим сохраненный ответ пользователя
    logging.debug(f"Stored response: {message}")

    return {"status": "success"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)