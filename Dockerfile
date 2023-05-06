FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CLOUD_SQL_USERNAME = 'root'
ENV CLOUD_SQL_PASSWORD = 'QjV"FGSh;M);H%LP'
ENV CLOUD_SQL_DATABASE_NAME = 'playlist'
ENV DB_LOCAL_HOST = '10.107.32.4:3306'

EXPOSE 8080

CMD ["python", "app.py"]