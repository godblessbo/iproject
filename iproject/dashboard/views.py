# coding=utf-8
import datetime
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def sign_up_view(req):
    return render_to_response('register.html')


def sign_in_view(req):
    nexturl = '/iproject/login/?next=' + req.GET['next']
    return render_to_response('login.html', {'nexturl': nexturl})


def sign_up(req):
    nexturl=req.GET['next']
    email = req.POST['email']
    username = req.POST['username']
    password = req.POST['password']
    first_name = req.POST['firstname']
    last_name = req.POST['lastname']
    # date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    User.objects.create_user(username=username, email=email, password=password)
    return home(req)


def sign_out(req):
    nexturl = '/iproject/home/'
    logout(req)
    return home(req)


def sign_in(req):
    nexturl = req.GET['next']
    if nexturl == '/iproject/login/':
        nexturl = '/iproject/home/'
    response = {}
    if not req.user.is_authenticated():
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(req, user)
                return redirect(nexturl)
            else:
                response['login_response'] = '您的账户未激活，请前往邮箱激活 '
        else:
            response['login_response'] = '请检查您的用户名和密码'
        return render_to_response('login.html', {'login_response': response['login_response']})
    else:
        return redirect(nexturl)


def home(req):
    return render_to_response('home.html')



def nextlink(req):
    nexturl=req.GET['next']