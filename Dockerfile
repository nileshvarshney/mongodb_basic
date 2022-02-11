FROM python:3.8.12-slim-buster

RUN pip install pymongo 
RUN pip install faker

RUN mkdir -p /home/app

COPY ./codes /home/demo/codes

CMD ["/usr/local/bin/python", "/home/demo/codes/py_mongo.py"]