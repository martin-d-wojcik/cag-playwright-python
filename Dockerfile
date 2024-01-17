FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

WORKDIR /app

COPY pages /app/pages
COPY tests /app/tests
COPY utils /app/utils

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt