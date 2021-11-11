# For more information, please refer to https://aka.ms/vscode-docker-python
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

EXPOSE 5000

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app