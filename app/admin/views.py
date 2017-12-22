from flask import render_template,request,url_for,session,flash,redirect,jsonify
from . import admin

@admin.errorhandler(404)
def page_not_found(e):
    return render_template('admin/404.html')

@admin.route('/404')
def page_404():
    return render_template('admin/404.html')

@admin.route('/')
def index():
    return render_template("admin/index.html")


@admin.route('/login')
def login():
    return render_template("admin/login.html")


@admin.route('/register')
def register():
    return render_template("admin/register.html")

@admin.route('/passwd')
def passwd():
    return render_template("admin/passwd.html")
