FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app/

RUN apt-get update

RUN apt-get install -y ca-certificates

EXPOSE 5000 
