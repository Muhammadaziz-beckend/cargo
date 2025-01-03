FROM python:3.11-alpine3.16

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000