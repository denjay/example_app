import os
import sys
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# print(sys.path[-1])
from model import db

app = Flask(__name__)
app.config.from_object('config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()