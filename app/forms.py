#encoding=utf8
#from flask_wtf import Form
#from wtforms import StringField, BooleanField, SubmitField, TextField
#from wtforms.validators import Required,DataRequired
#from flask import Flask,render_template
import flask
#引入模块
#from flask_wtf import FlaskForm,CsrfProtect
#如果输入的是字符串那么就用StringField,如果是整数那么就用IntegerField
#from wtforms import StringField,IntegerField
#验证方式
#from wtforms.validators import Length,EqualTo,InputRequired
from wtforms import Form, BooleanField, TextField, SubmitField, PasswordField, validators, StringField
from wtforms.validators import Length,EqualTo,InputRequired, Required


##file upload
class UploadForm(Form):
    filename=TextField('filename', [validators.Length(min=4, max=25)])
    submit = SubmitField(u'Upload')    


class LoginForm(Form):
    username=StringField(label='user',validators=[Required()])
    password=PasswordField(label='password',validators=[Required()])
    submit=SubmitField(label='commit')
    remember_me=BooleanField('remember_me',default=False)

#class RegistForm(FlaskForm):
#    username = StringField(validators=[Length(min=3,max=10,message=u"用户名长度有问题")])
#    password = StringField(validators=[Length(min=6,max=20)])
 #   age = IntegerField(validators=[InputRequired()])


#class MyForm(Form):
#    name = TextField('name', validators=[DataRequired()])
