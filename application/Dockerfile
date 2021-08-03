# base image
FROM python:3
RUN apt-get -y update
RUN apt-get -y install python3-pip
RUN apt-get install -y build-essential
COPY /application .
RUN pip3 install -r requirements.txt
