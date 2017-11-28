import models as db
import sys

conn = db.conn_db()
conn = conn.commit()
cur = conn.cursor()

username=sys.argv[1]
passwd=sys.argv[2]
sql=("select username,passwd from user where username='%s' and passwd='%s'") % (username,passwd)


try:
    cur.execute(sql)
    text=cur.fetchone()
    print text
except Exception,e:
    print "error:"+e

