FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install git && apt-get -y install python-pip && apt-get -y install libevent-dev python-all-dev

RUN pip install gevent pyzmq locustio

EXPOSE 8089

ADD . /code

CMD ["locust", "--host=http://localhost:5000", "-f", "/code/locustfile.py"]
