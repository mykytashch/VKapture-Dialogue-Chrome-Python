from pymongo import MongoClient

client = MongoClient('mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net/')

try:
    client.admin.command('ping')
    print("Пинговали вашу базу данных. Успешное подключение к MongoDB!")
except Exception as e:
    print(e)

db = client['question_database']

funny_questions = [
    {"QuestionID": 1, "QuestionText": "Если бы вы были фруктом, каким фруктом были бы и почему?"},
    {"QuestionID": 2, "QuestionText": "Какой был бы ваш суперспособ, если бы вам выпал шанс выбрать?"},
    {"QuestionID": 3, "QuestionText": "Как вы объясните цвет оранжевого чебурека?"},
    {"QuestionID": 4, "QuestionText": "Какой анекдот всегда вас заставляет смеяться?"},
    {"QuestionID": 5, "QuestionText": "Какое бы название вы дали своей автобиографии?"}
]

for i in range(5):
    collection_name = f"Questions_{i+1}"
    collection = db[collection_name]
    collection.insert_many(funny_questions)

    print(f"Создана коллекция вопросов: {collection_name}")

client.close()
