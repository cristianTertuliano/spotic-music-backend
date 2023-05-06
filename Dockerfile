FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CLOUD_SQL_USERNAME = 'root'
ENV CLOUD_SQL_PASSWORD = 'QjV"FGSh;M);H%LP'
ENV CLOUD_SQL_DATABASE_NAME = 'playlist'
ENV CLOUD_SQL_CONNECTION_NAME = 'grupo-11-384916:us-central1:spotmusic01'

EXPOSE 8080

CMD ["python", "app.py"]