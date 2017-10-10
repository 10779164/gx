import models as db


sql="select username,passwd from user"
db=db.conn_db()
db=db.conn()

db.execute(sql)
row=db.fetchall()
db.close()
print row
