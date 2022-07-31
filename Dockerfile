FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install sqlite3 && \
    pip install -r requirements.txt && \
    sqlite3 ./db/product_manager.db < ./db/product_manager.sql && \
    python console.py

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
