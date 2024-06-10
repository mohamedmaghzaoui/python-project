FROM python:3.11.9-alpine3.20
WORKDIR /app
COPY requirements.txt /app/
COPY bipEnv /app/
RUN pip install -r /app/requirements.txt