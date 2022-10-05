FROM python:3.10-slim

WORKDIR /tmp
COPY requirements/requirements.app.txt .
RUN pip install --no-cache-dir -r requirements.app.txt


COPY src/app /opt/app
WORKDIR /opt/app

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
