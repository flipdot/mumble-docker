

FROM python:3-alpine3.11

ARG VERSION=6.0

RUN apk add git zlib-dev libjpeg-turbo-dev gcc musl-dev opus-dev opus libmagic ffmpeg
COPY ./botamusique /botamusique


RUN cd /botamusique \
  && python3 -m venv venv \
  && venv/bin/pip install wheel \
  && venv/bin/pip install -r pymumble/requirements.txt \
  && venv/bin/pip install -r requirements.txt

CMD /botamusique/venv/bin/python /botamusique/mumbleBot.py --config /data/configuration.ini

VOLUME /music
VOLUME /data
