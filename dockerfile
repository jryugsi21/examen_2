FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install flask psycopg2-binary

COPY . .

EXPOSE 5000

CMD ["python","app.py"]