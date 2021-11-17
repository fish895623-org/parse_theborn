FROM python:3.8

WORKDIR /workspace
COPY ./ /workspace
RUN apt-get update >/dev/null&& apt-get install -y -q chromium-driver &&\
    /usr/local/bin/python3 -m pip install --no-cache-dir -r /workspace/requirements.txt
RUN chmod +x /workspace/chromedriver

CMD ["/usr/local/bin/python3 /workspace/src/main.py"]
