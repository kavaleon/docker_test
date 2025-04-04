FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

ENV FLASK_APP=run.py
EXPOSE 5000

RUN flask db upgrade

CMD ["flask", "run", "--host=0.0.0.0"]