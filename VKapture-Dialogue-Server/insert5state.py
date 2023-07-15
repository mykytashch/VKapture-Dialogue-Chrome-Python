from pymongo import MongoClient

client = MongoClient('mongodb+srv://tosniki91:N25kbverb@clustervkapture.b6tox4s.mongodb.net/')

try:
    client.admin.command('ping')
    print("Пинговали вашу базу данных. Успешное подключение к MongoDB!")
except Exception as e:
    print(e)

db = client['my_database']

state_collection = db['State']

for i in range(5):
    collection_name = f"Questions_{i+1}"
    collection = db[collection_name]

    # Получение количества вопросов в коллекции
    total_questions = collection.count_documents({})

    # Создание документа состояния для текущей коллекции
    state_doc = {
        "EmployeeID": i+1,
        "CurrentQuestionID": 1,
        "RemainingQuestions": total_questions - 1
    }

    # Вставка документа состояния в коллекцию состояния
    state_collection.insert_one(state_doc)

    print(f"Создан документ состояния для коллекции вопросов: {collection_name}")

client.close()
