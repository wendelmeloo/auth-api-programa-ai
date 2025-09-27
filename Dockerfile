FROM python:3.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends libffi-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV FLASK_APP=wsgi.py \
    FLASK_ENV=development 

EXPOSE 5001

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]