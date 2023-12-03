# Використання офіційного образу Python
FROM python:3.9-slim

# Встановлення залежностей
RUN pip install Flask MongoEngine docker

# Копіювання вихідного коду в контейнер
COPY ./app /app
WORKDIR /app

# Встановлення точки входу
ENTRYPOINT ["python"]
CMD ["main.py"]
