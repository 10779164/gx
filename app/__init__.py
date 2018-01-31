from flask import Flask

app=Flask(__name__)
app.config.from_pyfile('/flask/gx/config.py')

from flask_sqlalchemy import SQLAlchemy
DB=SQLAlchemy(app)
from app import models

#from app import views
from app import hello
from app.controller import test,views
from admin import admin
from admin import views

app.register_blueprint(admin,url_prefix='/admin')


