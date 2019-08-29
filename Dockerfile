FROM ubuntu

RUN apt-get update && apt-get install python-virtualenv python-pip python-mysqldb -y

COPY app/ /var/www/demo
RUN pip install -r /var/www/demo/requirements.txt  
RUN virtualenv /var/www/demo/.venv

EXPOSE 80
WORKDIR /var/www/demo
CMD ["python", "demo.py"]
