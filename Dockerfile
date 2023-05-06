FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app