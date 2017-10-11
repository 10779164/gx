import MySQLdb

class conn_db():
    def conn(self):
    	conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    	conn.select_db('hosts')
    	cur=conn.cursor()
    	return cur


#sql="select hostname from host"
#a=db()
#a=a.conn()

#a.execute(sql)
#row=a.fetchone()
#print row[0]
