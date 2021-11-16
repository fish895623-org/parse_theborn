FROM python:3.8

COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y chromium-browser
RUN python3 -m pip install -U pip &&\
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt &&\
    rm -rf /tmp/requirements.txt