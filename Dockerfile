FROM python:3.8

WORKDIR /workspace
RUN pip install -r /workspace/requirements.txt

CMD ["python3 src/main.py"]