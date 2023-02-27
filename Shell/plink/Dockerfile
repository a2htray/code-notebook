FROM ubuntu:18.04

WORKDIR /usr/src/plink

RUN apt update && apt install -y wget unzip
RUN wget https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20230116.zip && \
    unzip plink_linux_x86_64_20230116.zip -d ./ && \
    rm plink_linux_x86_64_20230116.zip && \
    ln -s $(pwd)/plink /usr/local/bin/plink

ENTRYPOINT ["/usr/local/bin/plink"]
