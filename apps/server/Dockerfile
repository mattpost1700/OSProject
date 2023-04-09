FROM python:3.8-slim-buster

ARG PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
# CMD ["python", "-m", "uvicorn", "main:app", "--proxy-headers", "--port", "8000"]
