FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install pyTelegramBotApi
RUN pip install -U aiogram

COPY . .

CMD ["python3", "bot.py"]