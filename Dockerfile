FROM python:2.7

MAINTAINER yuyang <yuyang0805@gmail.com>

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD src /code

ENTRYPOINT ["gunicorn", "-w 4", "-b 0.0.0.0:8070", "app:app"]
