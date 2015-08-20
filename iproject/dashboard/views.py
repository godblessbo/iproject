# coding=utf-8

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def showPage(req):
    pagehtml = req.REQUEST.get('pagehtml')
    username = getusername(req)
    if pagehtml == None or pagehtml == '':
        pagehtml = 'home.html'
    return render_to_response(pagehtml, {'username': username})


def getusername(req):
    username = 'guest'
    if req.user.is_authenticated():
        username = req.user.username
    else:
        sign_in_view(req)
    return username


def sign_in_view(req):
    nexturl = '/iproject/login/?next=' + req.GET['next']
    return render_to_response('login.html', {'nexturl': nexturl})


def sign_up(req):
    email = req.POST['email']
    username = req.POST['username']
    password = req.POST['password']
    first_name = req.POST['firstname']
    last_name = req.POST['lastname']
    # date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    User.objects.create_user(username=username, email=email, password=password)
    user = authenticate(username=username, password=password)
    login(req, user)
    return render_to_response('home.html')


def sign_out(req):
    logout(req)
    return render_to_response('home.html')


def sign_in(req):
    nexturl = req.GET['next']
    if nexturl == '/iproject/login/':
        nexturl = '/iproject/profile/'
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
