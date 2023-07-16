from flask import Flask, request, send_file, jsonify
from pymongo import MongoClient, ASCENDING
from bson import ObjectId
import json

app = Flask(__name__)
client = MongoClient('mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net/')

# JSON-кодировщик для обработки ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)  # Преобразование ObjectId в строку
        return super().default(o)

# Обработчик для загрузки состояния опроса
@app.route('/load_state', methods=['POST'])
def load_state():
    data = request.json
    employee_id = data.get('EmployeeID')

    db = client['state_database']
    state_collection = db['State']
    state = state_collection.find_one({'EmployeeID': employee_id}, {'_id': 0})

    if state:
        response_data = {
            'CurrentQuestionID': state.get('CurrentQuestionID'),
            'RemainingQuestions': state.get('RemainingQuestions')
        }
        response_json = json.dumps(response_data, cls=JSONEncoder, indent=2)  # Преобразование в отформатированную строку JSON
        return response_json, 200, {'Content-Type': 'application/json'}  # Установка правильного заголовка Content-Type
    else:
        new_state = {
            'EmployeeID': employee_id,
            'CurrentQuestionID': 1,
            'RemainingQuestions': 100
        }
        state_collection.insert_one(new_state)
        response_json = json.dumps(new_state, cls=JSONEncoder, indent=2)  # Преобразование в отформатированную строку JSON
        return response_json, 200, {'Content-Type': 'application/json'}  # Установка правильного заголовка Content-Type



# Обработчик для загрузки вопросов для определенного EmployeeID
@app.route('/load_questions', methods=['POST'])
def load_questions():
    data = request.json
    employee_id = data.get('EmployeeID')
    start_from = data.get('startFrom', 0)  # startFrom - это ID последнего вопроса, который был задан пользователю

    db = client['question_database']
    questions_collection = db[f'Questions_{employee_id}']
    questions = list(questions_collection.find(
        {'QuestionID': {'$gt': start_from}},
        {'QuestionText': 1, 'QuestionID': 1, '_id': 0}
    ).limit(100))

    return jsonify({'questions': questions})


# Обработчик для получения ответов от клиента и записи их в базу данных
@app.route('/store_responseCOMENT', methods=['POST'])
def store_responseCOMENT():
    data = request.json
    employee_id = data.get('EmployeeID')
    processed_question_id = data.get('ProcessedQuestionID')
    processed_question_text = data.get('ProcessedQuestionText')
    answer_text = data.get('AnswerText')

    db = client['response_database']
    responses_collection = db[f'Responses_{employee_id}']
    responses_collection.insert_one({
        'ProcessedQuestionID': processed_question_id,
        'ProcessedQuestionText': processed_question_text,
        'AnswerText': answer_text
    })

    return 'Response recorded successfully', 200


# Обработчик для сброса опроса
@app.route('/reset_survey', methods=['POST'])
def reset_survey():
    data = request.json
    employee_id = data.get('EmployeeID')

    db = client['your_database']
    responses_collection = db[f'Responses_{employee_id}']
    responses_collection.delete_many({})

    state_collection = db['State']
    state_collection.update_one({'EmployeeID': employee_id}, {'$set': {'CurrentQuestionID': 0, 'RemainingQuestions': 0}}, upsert=True)

    return 'Survey reset successfully', 200

# Обработчик для скачивания истории ответов
@app.route('/download_history', methods=['POST'])
def download_history():
    data = request.json
    employee_id = data.get('EmployeeID')

    db = client['your_database']
    responses_collection = db[f'Responses_{employee_id}']
    responses = list(responses_collection.find({}, {'ProcessedQuestionID': 1, 'ProcessedQuestionText': 1, 'AnswerText': 1, '_id': 0}))

    file_contents = ''
    for response in responses:
        processed_question_id = response.get('ProcessedQuestionID')
        processed_question_text = response.get('ProcessedQuestionText')
        answer_text = response.get('AnswerText')
        file_contents += f'ProcessedID: {processed_question_id}\nQuestionText: {processed_question_text}\nAnswerText: {answer_text}\n\n'

    with open('result.txt', 'w') as file:
        file.write(file_contents)

    return send_file('result.txt', as_attachment=True)


@app.route('/store_response', methods=['POST'])
def store_response():
    data = request.get_json()  # получаем JSON из запроса
    message = data.get('message')  # извлекаем поле 'message' из данных JSON
    print(message)  # выводим сообщение в консоль
    return {}, 200  # возвращаем ответ со статусом 200 (OK)


if __name__ == '__main__':
    app.json_encoder = JSONEncoder  # Использование кастомного JSON-кодировщика
    app.run(host='0.0.0.0', port=5000, debug=True)