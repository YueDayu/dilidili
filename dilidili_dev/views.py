from django.shortcuts import render
from django.http import HttpResponseRedirect
from dilidili_dev.admin import UserCreationForm
from django.contrib import auth
from dilidili_dev.users import User


def register(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect("/admin")
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid() and request.POST['password1'] and len(request.POST['password1']) >= 6:
            form.save()
            # user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            # auth.login(request, user)
            # TODO: 注册后自动登陆
            return HttpResponseRedirect("/admin")
        else:
            username = request.POST['username'] if request.POST['username'] else ""
            password1 = request.POST['password1'] if request.POST['password1'] else ""
            password2 = request.POST['password2'] if request.POST['password2'] else ""
            name = request.POST['name'] if request.POST['name'] else ""
            email = request.POST['email'] if request.POST['email'] else ""
            describe = request.POST['describe'] if request.POST['describe'] else ""
            error_msg = "错误"
            if not username:
                error_msg = "请输入用户名"
            elif not (password1 and password2):
                error_msg = "请输入密码"
            elif not name:
                error_msg = "请输入昵称"
            elif not email:
                error_msg = "请输入邮箱"
            elif not describe:
                error_msg = "请输入个人描述"
            elif password1 != password2:
                error_msg = "两次密码不一致"
            elif len(password1) < 6:
                error_msg = "密码长度小于6位"
            elif User.objects.filter(username=username):
                error_msg = "用户名已经存在"
            elif User.objects.filter(email=email):
                error_msg = "邮箱已经注册"
            elif User.objects.filter(name=name):
                error_msg = "昵称已经被使用"
            return render(request, "registration/register.html", {'error': error_msg,
                                                                  'username': username,
                                                                  'name': name,
                                                                  'email': email,
                                                                  'describe': describe})
    return render(request, "registration/register.html")


def index(request):
    return render(request, "base.html")
