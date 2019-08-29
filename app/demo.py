from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import socket

app = Flask(__name__)
os.environ['DATABASE_URI'] = 'mysql://amadeu:pitagoras@db-amadeu/dexter'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
hostname = socket.gethostname()


@app.route('/')
def index():
    return 'Ola, eu sou o Amadeu Pitagoras e esse eh o container %s!\n' % hostname


@app.route('/db')
def dbtest():
    try:
        db.create_all()
    except Exception as e:
        return e.message + '\n'
    return 'Database Connected from %s!\n' % hostname


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
