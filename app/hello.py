from app import app
from . import DB
from models import user

@app.route('/hello')
def hhh():
    username ='gx'
    result = user.query.filter(username==username).first()
    return result.email 
