#encoding=utf8
import os
import sys
reload(sys)    
sys.setdefaultencoding('utf8')
import flask
import forms
import MySQLdb
from app import app
from flask import render_template,request,url_for,session,request,flash,redirect
#from app.forms import LoginForm,RegistForm
from werkzeug import secure_filename
import models as db
import image

@app.route('/')
@app.route('/index.html')
def index():
    user='flask'
    #print request.method
    return render_template('index.html',title='hello',user=user)


@app.route('/test') 
def test():
    #print request
    return render_template('test.html',result=request.remote_addr)


@app.route('/ip') 
def ip():
    #print request
    return render_template('ip.html',result=request.remote_addr)


@app.route('/user')
@app.route('/user/<user>')
def user(user=None):
    return render_template('index.html',title='hello',user=user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    #连接数据库
    cur=db.conn_db()
    cur=cur.conn()
    #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
    #print request.cookies
    if request.method == 'POST':
        #form = forms.LoginForm()
        #print '\n'.join(['%s:%s' % item for item in form.__dict__.items()])
    	username=request.form.get('username')
    	password=request.form.get('password')
	sql=("select passwd from user where username='%s'") % username
	cur.execute(sql)
        result=cur.fetchone()
	cur.close()
    	#if username==str(result[0]) and password==str(result[1]):
	if password==result[0]:
	    return redirect(url_for('host'))
    	else:
	    error="*登录失败：用户名或密码错误！"
    	    return render_template('index.html',error=error)
    else:
	return render_template('index.html',error='')

#@app.route('/form',methods=["GET","POST"])
#def form():
#    if request.method == "GET":
#        return render_template("index.html")
#    else:
#        form = RegistForm(request.form)
#        if form.validate():
#            username = form.username.data
#            password =form.passwd.data
#            print username,password
#            return u"登录成功"
#        else:
#            print form.errors
#            return u"错误"

@app.route('/success')
def success():
    #return '<h1>Success</h1>'
    return render_template('test.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/for')
def foryy():
    return render_template('for.html')


@app.route('/wtf')
def wtf():
    return render_template('wtf.html')

#@app.route('/submit', methods=('GET', 'POST'))
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return redirect('/success')
#    return render_template('submit.html', form=form)


#@app.route('/uploads',methods=('GET','POST'))
#def upload_file():
    #form = forms.UploadForm()
    #print 1
    #if request.method == 'POST':
        #print 2
        #file = form.filename.data
        #print request.form['filename']
        #flash('upload success!')
        #print file
        #print request.method
        #if file and allowed_file(file.filename):
        #    filename = secure_filename(file.filename)
        #    file.save(os.path.join(app.config['file_path'],filename))
        #    #return redirect(url_for('upload_file',filename=filename))
        #    return render_template('index.html')


###upload -file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload',methods=('GET','POST'))
def upload():
    if request.method == 'POST':
        #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
        try:
            f = request.files['filename']
            upload_path=os.path.join('/flask/gx/uploads',secure_filename(f.filename))
            f.save(upload_path)
            result="提示：文件"+f.filename+"上传成功"
            #f.save(os.path.join(app.config['file_path'],'/',secure_filename(f.filename))
            #return redirect(url_for('upload'))
            return render_template('upload_file.html',result=result)
        except Exception,e:
            result="文件上传失败："+str(e)
            return render_template('upload_file.html', result=result)
    else:
        return render_template('upload_file.html',result=None)


###图片转换
@app.route('/image',methods=('GET','POST'))
def upload_image():
    if request.method == 'POST':
        #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
        try:
            f = request.files['filename']
            print f.filename
            upload_path=os.path.join('/flask/gx/uploads/images/',secure_filename(f.filename))
            f.save(upload_path)
            img_src="/flask/gx/uploads/images/"+str(f.filename)
    	    filename=f.filename
	    image.image_tran(img_src,filename)
            #result="提示：文件"+f.filename+"上传成功"
            #f.save(os.path.join(app.config['file_path'],'/',secure_filename(f.filename))
            #return redirect(url_for('upload'))
            return render_template('image.html', result=f.filename)
        except Exception,e:
            result="文件上传失败：仅支持图片格式~~"
            return render_template('upload_image.html', result=result)
    else:
        return render_template('upload_image.html',result='')


###host
#@app.route('/host')
def host1():
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    cur=conn.cursor()
    conn.select_db('system')
    cur.execute("select hostname from host")
    hostname=cur.fetchone()
    cur.execute("select hostip from host")
    hostip=cur.fetchone()
    cur.execute("select passwd from host")
    passwd=cur.fetchone()
    passwd=passwd
    cur.close()
    conn.close()
    return render_template('host.html',hostname=hostname[0],hostip=hostip[0],passwd=passwd[0])
    

###特效网页
@app.route('/html5')
@app.route('/html5/')
def html5():
    return render_template("html5.html")

@app.route('/html5/<name>')
def magic(name=None):
    if name == "3DFire":
    	return render_template("3DFire.html")
    elif name == "paomo":
	return render_template('paomo.html')
    elif name == "3DFlower":
  	return render_template('3DFlower.html')
    elif name == "shaizi":
        return render_template('shaizi.html')
    elif name == "tree":
        return render_template('tree.html')
    elif name == "pac-man":
        return render_template('pac-man.html')
    elif name == "html5":
        return render_template('html5.html')
    else:
	return render_template("html5.html")



#host
@app.route('/host')
def host():
    #连接数据库
    cur=db.conn_db()
    cur=cur.conn()
    
    sql="select * from host"
    cur.execute(sql)
    record=cur.fetchall()
    cur.close()
    return render_template('host.html',record=record)


#test
@app.route('/h')
@app.route('/h/<hostname>')
def h(hostname=None):
    if hostname==None:
    	return render_template('h.html')
    else:
	#连接数据库
    	cur=db.conn_db()
    	cur=cur.conn()

    	sql="select * from host where hostname='%s'" % hostname
    	cur.execute(sql)
    	record=cur.fetchall()
    	cur.close()
    	return render_template('hshow.html',record=record)

@app.route('/h/h1')
@app.route('/h/h1.html')
def h1():
    cur=db.conn_db()
    cur=cur.conn()

    sql="select distinct hostname from host"
    cur.execute(sql)
    record=cur.fetchall()
    cur.close()
    return render_template('h1.html',record=record)
       
@app.route('/h/h_top.html')
def h_top():
    return render_template('h_top.html') 

 
#添加主机
@app.route('/host_add', methods = ['GET', 'POST'])
@app.route('/hadd.html')
def host_add():
    #连接数据库
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    cur=conn.cursor()
    conn.select_db('hosts')
    #
    if request.method == 'POST':
	hostname=request.form.get('hostname')
	ip=request.form.get('ip')
	passwd_root=request.form.get('passwd_root')
	passwd_db=request.form.get('passwd_db')
	ssh_port=request.form.get('ssh_port')
	try:
    	    sql=("insert into host value(NULL,'%s','%s','%s','%s','%s')") % ( hostname, ip, passwd_root, passwd_db, ssh_port)
	    cur.execute(sql)
	    conn.commit()
	    #cur.close()
	    result="**提交成功"
	    return render_template('hadd.html',result=result)
	except Exception,e:
	    conn.rollback()
	    result='"**submit error:'+str(e)+'"'
	    return render_template('hadd.html',result=result)
	cur.close()
    else:
 	return render_template('hadd.html',result='')


@app.route('/host_del',methods = ['GET', 'POST'])
@app.route('/host_del_search',methods = ['GET', 'POST'])
def host_del():
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    cur=conn.cursor()
    conn.select_db('hosts')
    if request.method == 'POST':
    	value=request.form.get('host')
	sql=("select * from host where hostname='%s' or ip='%s'") % (value,value) 
	cur.execute(sql)

	field=[]
	for row in cur.description:
		field.append(row[0])
		

	record=cur.fetchall()
	conn.commit()
	conn.close()
	#print record
	if len(record) == 0:
	    result=""
	    return render_template('host_del.html',result=result)
	else:
	    result=dict(zip(field,record[0]))
	    return render_template('host_del.html',result=result)
    else:
	return render_template('host_del_search.html',result='')


@app.route('/del_host',methods = ['POST'])
def del_host():
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    cur=conn.cursor()
    conn.select_db('hosts') 
    value=request.form.to_dict()
    print value
    for key in value:
        ip=key    
    
    ip=ip.split(":")[1]
    sql=("delete from host where ip='%s'") % ip
    cur.execute(sql)   
    record=cur.fetchall()
    conn.commit()
    conn.close()
    
    return render_template('host_del_search.html') 
       


##查询主机
@app.route('/host_query',methods=['GET','POST'])
def host_query():
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost',charset='utf8')
    cur=conn.cursor()
    conn.select_db('hosts')
    if request.method == 'POST':
        value=request.form.get('host')
        sql=("select * from host where hostname='%s' or ip='%s'") % (value,value)
        cur.execute(sql)

        field=[]
        for row in cur.description:
                field.append(row[0])


        record=cur.fetchall()
        conn.commit()
        conn.close()
        #print record
        if len(record) == 0:
            result=""
            return render_template('host_query.html',result=result)
        else:
            result=dict(zip(field,record[0]))
            return render_template('host_query.html',result=result)
    else:
        return render_template('host_query.html',result='default')


@app.route('/ajax_test')
def ajax_test():
    return render_template('ajax.html')

@app.route('/ajax',methods=['POST'])
def ajax():
    #form=to_dict(request.form)
    data=request.form.to_dict()
    print data
    for key in data:
 	print key
    return render_template('index.html')









