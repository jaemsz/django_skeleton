FROM python:alpine3.19

WORKDIR /opt/skeleton

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /opt/skeleton/requirements.txt

RUN pip install -r requirements.txt

COPY ./main.sh /opt/skeleton/main.sh

COPY . /opt/skeleton/

RUN ["/opt/skeleton/main.sh"]
