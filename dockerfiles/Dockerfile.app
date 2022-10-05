FROM python:3.10-slim

WORKDIR /tmp
COPY requirements/requirements.app.txt .
RUN pip install --no-cache-dir -r requirements.app.txt

COPY src/job /opt/app
WORKDIR /opt/app