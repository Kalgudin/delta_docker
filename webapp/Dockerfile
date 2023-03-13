FROM python:3.8.3-alpine
#RUN apt-get update -y
#RUN apt-get upgrade -y

WORKDIR /webapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src ./src

CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]

