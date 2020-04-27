FROM python:3.7
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn fampay.wsgi:application — bind 0.0.0.0:8000 — workers 3