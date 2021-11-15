FROM python:3.8

WORKDIR /workspace
COPY ./ /workspace
RUN pip install -r /workspace/requirements.txt
RUN chmod +x /workspace/chromedriver

CMD ["python3 src/main.py"]