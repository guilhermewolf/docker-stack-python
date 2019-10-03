FROM python:3.6-alpine3.10

COPY app/ /var/www/demo
RUN pip install -r /var/www/demo/requirements.txt && pip install virtualenv
RUN virtualenv  /var/www/demo/.venv

EXPOSE 80
WORKDIR /var/www/demo
CMD ["python", "demo.py"]
