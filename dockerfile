FROM python:3.14-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]