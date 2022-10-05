FROM python:3.10-slim

WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/job /opt/app
WORKDIR /opt/app