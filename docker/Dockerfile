FROM python:3.7

# Metadata
LABEL base.image="python:3.7"
LABEL software="JTracker Account Management Service"
LABEL website="https://github.com/jtracker-io/jt-ams"

# File Author / Maintainer
MAINTAINER Junjun Zhang <junjun.ca@gmail.com>

USER root

RUN wget -O tmp.tar.gz -t 10 https://github.com/jtracker-io/jt-ams/archive/0.2.0a9.tar.gz && \
    mkdir -p /srv/jt-ams && \
    tar -C /srv/jt-ams --strip-components 1 -zxf tmp.tar.gz && \
    pip3 install -r /srv/jt-ams/requirements.txt

CMD ["python3", "/srv/jt-ams/app.py"]
