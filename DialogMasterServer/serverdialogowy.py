from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net/')

# Обработчик для получения ответов от клиента и записи их в базу данных
@app.route('/store_response', methods=['POST'])
def store_response():
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


# Обработчик для загрузки состояния опроса
@app.route('/load_state', methods=['POST'])
def load_state():
    data = request.json
    employee_id = data.get('EmployeeID')

    db = client['state_database']
    state_collection = db['State']
    state = state_collection.find_one({'EmployeeID': employee_id}, {'_id': 0})
    if state:
        return {
            'CurrentQuestionID': state.get('CurrentQuestionID'),
            'RemainingQuestions': state.get('RemainingQuestions')
        }, 200
    else:
        # Создание нового состояния, если не найдено
        state_collection.insert_one({
            'EmployeeID': employee_id,
            'CurrentQuestionID': 0,
            'RemainingQuestions': 100  # Общее количество вопросов
        })
        return {
            'CurrentQuestionID': 0,
            'RemainingQuestions': 100
        }, 200


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 (debug=True)
    app.run()
