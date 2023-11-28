FROM python:3.11-alpine

WORKDIR /app

COPY action.py .

ENTRYPOINT ["python3", "/app/action.py"]
