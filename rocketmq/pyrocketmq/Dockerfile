FROM ubuntu:18.04

RUN apt update && apt install -y software-properties-common
RUN apt update && add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3-pip
RUN pip3 install rocketmq-client-python rocketmq

CMD ["tail", "-f", "/var/log/dpkg.log"]
