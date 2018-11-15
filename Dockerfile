FROM python:3

COPY requirements.txt /tmp/.

RUN pip install -r /tmp/requirements.txt

WORKDIR /

COPY ./app/. /

EXPOSE 8881
EXPOSE 8882
EXPOSE 8883

CMD [ "python", "__main__.py", "service_a", "service_b", "service_c" ]
