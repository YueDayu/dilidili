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
        if user is not None:
            # print(dir(user))
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return render(request, "registration/login.html", {'error': "该用户已经被禁止登陆",
                                                                   'username': username})
        else:
            return render(request, "registration/login.html", {'error': "用户名或密码不正确",
                                                               'username': username})
    else:
        return render(request, "registration/login.html")
