FROM nikolaik/python-nodejs:python3.10-nodejs19

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 channelbot.py
