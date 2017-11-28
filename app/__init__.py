from flask import Flask

app=Flask(__name__)
app.config.from_pyfile('/flask/gx/config.py')

#from app import views
from app import hello
from app.controller import test,views



