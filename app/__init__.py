from flask import Flask

app=Flask(__name__)
app.config.from_pyfile('/flask/gx/config.py')

#from app import views
from app import hello
from app.controller import test,views
from admin import admin
from admin import views

app.register_blueprint(admin,url_prefix='/admin')


