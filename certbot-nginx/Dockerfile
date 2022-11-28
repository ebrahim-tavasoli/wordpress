FROM python:3.9.15-bullseye

RUN pip install certbot-nginx

WORKDIR /app

COPY ./entrypoint.py .

CMD [ "python3", "entrypoint.py" ]
