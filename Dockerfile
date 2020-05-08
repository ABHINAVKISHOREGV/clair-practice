FROM alpine:latest
RUN apk add --update-cache \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

ONBUILD COPY requirements.txt .
ONBUILD RUN virtualenv /env && /env/bin/pip install -r /requirements.txt

CMD ["/env/bin/python", "--version"]
