# Використання офіційного образу Python
FROM python:3.9-slim

# Встановлення залежностей
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Копіювання вихідного коду в контейнер
COPY ./app /app
WORKDIR /app

# Встановлення точки входу
ENTRYPOINT ["python"]
CMD ["main.py"]
