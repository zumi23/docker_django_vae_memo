FROM python:3.8.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project
RUN pip install -r requirements.txt
