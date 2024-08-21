FROM python:3.12.4

WORKDIR /app

RUN pip install python-dotenv python-decouple requests

COPY . .

CMD ["sh", "-c", "sleep 10 && python ./co/uniquindio/edu/app.py"]
