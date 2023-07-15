# Используйте базовый образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта в контейнер
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY . .

# Открываем порт, на котором будет работать сервер Flask
EXPOSE 5000

# Запускаем сервер Flask
CMD ["python", "serverdialogowy.py"]
