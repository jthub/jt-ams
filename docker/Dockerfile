FROM ubuntu:16.04

# Metadata
LABEL base.image="ubuntu:16.04"
LABEL software="JTracker Account Management Service"
LABEL website="https://github.com/jthub/jt-ams"

# File Author / Maintainer
MAINTAINER Junjun Zhang <junjun.ca@gmail.com>

USER root

RUN apt-get -yqq update && \
    apt-get -yqq install curl

RUN curl -sSL -o tmp.tar.gz --retry 10 https://github.com/jthub/jt-ams/archive/0.2.0a6.tar.gz && \
    mkdir -p /opt/jt-ams && \
    tar -C /opt/jt-ams --strip-components 1 -zxf tmp.tar.gz && \
    apt-get -yqq install python3-pip && \
    pip3 install --upgrade pip  && \
    pip3 install -r /opt/jt-ams/requirements.txt

CMD ["/usr/bin/python3", "/opt/jt-ams/app.py"]
