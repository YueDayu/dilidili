__author__ = 'Yue Dayu'

from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def login(request, error_msg=""):
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
        return render(request, "registration/login.html", context=error_msg or {})


def change_password(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            username = request.user.username
            old_password = request.POST.get('password', '')
            new_password1 = request.POST.get('password1', '')
            new_password2 = request.POST.get('password2', '')
            user = auth.authenticate(username=username, password=old_password)
            if user is not None:
                if new_password1 != new_password2:
                    return render(request, "registration/change-password.html", {'error': "两次密码长度不同"})
                if len(new_password1) < 6 or len(new_password2) < 6:
                    return render(request, "registration/change-password.html", {'error': "新密码长度太短"})
                user.set_password(new_password1)
                user.save()
                return HttpResponseRedirect('/home/')
            else:
                return render(request, "registration/change-password.html", {'error': "密码错误"})
        else:
            return render(request, "registration/change-password.html")
    else:
        return HttpResponseRedirect("/")
