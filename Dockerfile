FROM ubuntu

LABEL classifier_version=1.0.1
LABEL owner="Bharat Bhalla Org"

RUN apt-get update && apt-get install -y python3-pip 

WORKDIR /model

COPY model .

RUN pip3 install -r requirements.txt

EXPOSE 8100

ENV FLASK_APP=model.py

CMD ["python3","-m","flask","run","--host=0.0.0.0","--port=8100"]