FROM python:3.6

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

COPY . /app/
