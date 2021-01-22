FROM ubuntu:latest

USER root

ENV AWS_ACCESS_KEY_ID test
ENV AWS_SECRET_ACCESS_KEY test

RUN apt update && apt -y install curl gnupg && curl -sL https://deb.nodesource.com/setup_14.x  | bash - && apt -y install nodejs

COPY package.json .

RUN npm install -g serverless && npm install

RUN apt -y install software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt update && apt -y install python3.8 && apt -y install python3-pip
