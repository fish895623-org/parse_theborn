RUN ubuntu:20.04

COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y python3.8 python3-pip chromium-chromedriver
RUN python3 -m pip install -U pip &&\
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt &&\
    rm -rf /tmp/requirements.txt