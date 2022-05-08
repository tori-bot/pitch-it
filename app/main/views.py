from django.shortcuts import render
from ..models import User,Comment
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from . import main

@main.route('/')
def index():
    title='Pitch it...One minute could change your life.'
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)



# @main.route('/comment',methods=['GET','POST'])
# @login_required
# def new_comment(identify):