from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,  MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)