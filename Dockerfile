FROM python:3.8

WORKDIR /workspace
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update >/dev/null&& apt-get install -y -qq chromium-driver
RUN /usr/local/bin/python3 -m pip install --no-cache-dir -r /tmp/requirements.txt
RUN /usr/local/bin/python3 -m pip install --no-cache-dir black
