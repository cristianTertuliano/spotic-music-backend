FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CLOUD_SQL_USERNAME=playuser
ENV CLOUD_SQL_PASSWORD=123456
ENV CLOUD_SQL_DATABASE_NAME=playlist
ENV DB_HOST=db
ENV APP_NAME=backend

EXPOSE 8080

CMD ["python", "app.py"]