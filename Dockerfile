FROM ubuntu

RUN apt-get update && apt-get install -y
\
python-pip 

COPY model .

WORKDIR /model

RUN pip install -r requirements.txt

EXPOSE 8100

CMD ["python","-m","flask","run","--host=0.0.0.0","--port=8100"]