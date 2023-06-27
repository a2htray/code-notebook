FROM ubuntu:18.04

LABEL maintainer_name="a2htray"
LABEL maintainer_email="a2htray@outlook.com"

RUN apt update && apt install -y openjdk-8-jdk wget unzip

RUN mkdir /app && chmod g+rw /app

WORKDIR /app

RUN useradd -rm -d /home/rocketmq -s /bin/bash -g root -G sudo -u 1001 rocketmq
USER rocketmq

RUN wget https://archive.apache.org/dist/rocketmq/4.5.2/rocketmq-all-4.5.2-bin-release.zip && \
    unzip rocketmq-all-4.5.2-bin-release.zip && \
    echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc && \
    echo 'export PATH=$PATH:/app/rocketmq-all-4.5.2-bin-release/bin' >> ~/.bashrc


COPY ./scripts /home/rocketmq/scripts

WORKDIR /home/rocketmq

VOLUME /home/rocketmq/logs

EXPOSE 5748

ENTRYPOINT ["./scripts/entrypoint.sh"]

