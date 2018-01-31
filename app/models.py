from . import DB

class user(DB.Model):
    __tablename__='user'
    userid = DB.Column(DB.Integer,primary_key=True,autoincrement=True)
    username = DB.Column(DB.String(20))
    passwd = DB.Column(DB.String(30))
    email = DB.Column(DB.String(20))


class test(DB.Model):
    __tablename__='test'
    userid = DB.Column(DB.Integer,primary_key=True,autoincrement=True)
    username = DB.Column(DB.String(20))


