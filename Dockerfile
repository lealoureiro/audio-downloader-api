FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/
ENV LIBRARY_DIR=/music

# install dependencies
RUN apk update
RUN apk add ffmpeg
RUN pip3 install --upgrade pip

# install app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app

VOLUME ["/music"]