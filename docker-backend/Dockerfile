FROM python:3.11 as builder

WORKDIR /app
RUN pip install poetry 

COPY . /app

CMD ["sh", "-c", "poetry install && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]

