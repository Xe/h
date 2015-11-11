FROM python:2

ADD . /h
WORKDIR /h
RUN ./env.sh

ONBUILD ADD config /h/config
CMD ./run.sh
