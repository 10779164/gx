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


@app.route('/')
@app.route('/index.html')
def index():
    user='flask'
    print request.method
    return render_template('index.html',title='hello',user=user)

@app.route('/user')
@app.route('/user/<user>')
def user(user=None):
    return render_template('index.html',title='hello',user=user)


@app.route('/test')
def test():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
    #print request.cookies
    if request.method == 'POST':
    #form = forms.LoginForm()
    #print '\n'.join(['%s:%s' % item for item in form.__dict__.items()])
    	username=request.form.get('username')
    	password=request.form.get('password')
    	if username=="root" and password=="flasker0115":
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


###host
@app.route('/host')
def host():
    conn=MySQLdb.connect(user='root',passwd='flasker0115',host='localhost')
    cur=conn.cursor()
    conn.select_db('system')
    cur.execute("select hostname from host")
    hostname=cur.fetchone()
    cur.execute("select hostip from host")
    hostip=cur.fetchone()
    cur.execute("select passwd from host")
    passwd=cur.fetchone()
    cur.close()
    conn.close()
    return render_template('host.html',hostname=hostname[0],hostip=hostip[0],passwd=passwd[0])
    

###特效网页
@app.route('/magic/<name>')
def magic(name=None):
    if name == "3DFire":
    	return render_template("3DFire.html")
    elif name == "paomo":
	return render_template('paomo.html')
    else:
	return render_template("404.html")


@app.route('/paomo')
def paomo():
    return render_template('paomo.html')









