FROM python:3.8-slim-buster

ARG PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# apt-get update && apt-get install procps
ENTRYPOINT ["python", "main.py"]
# CMD ["python3", "main.py"]
