FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY flashcard_generator.py .

CMD ["python", "flashcard_generator.py"]
