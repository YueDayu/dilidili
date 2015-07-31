__author__ = 'Yue Dayu'

from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            if not user.is_active:
                error_msg = "该用户已经被禁止登陆"
            else:
                error_msg = "用户名或密码不正确"
            return render(request, "registration/login.html", {'error': error_msg,
                                                               'username': username})
    else:
        return render(request, "registration/login.html")
