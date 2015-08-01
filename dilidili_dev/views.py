from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_http_methods
from dilidili_dev.admin import UserCreationForm
from dilidili_dev.video_upload import VideoUploadForm
from dilidili_dev.models import Video
from django.contrib import auth
from dilidili_dev.users import User


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid() and request.POST['password1'] and len(request.POST['password1']) >= 6:
            form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
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
                username = ""
            elif User.objects.filter(email=email):
                error_msg = "邮箱已经注册"
                email = ""
            elif User.objects.filter(name=name):
                error_msg = "昵称已经被使用"
                name = ""
            return render(request, "registration/register.html", {'error': error_msg,
                                                                  'username': username,
                                                                  'name': name,
                                                                  'email': email,
                                                                  'describe': describe})
    return render(request, "registration/register.html")


@require_http_methods(["GET"])
def index(request):
    return render(request, "index/index.html")


@require_http_methods(["GET"])
def personal(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'personal/personal.html', {'user': user})


@require_http_methods(["GET"])
def home(request):
    if request.user.is_authenticated():
        return render(request, 'home/home.html', {'user': request.user})
    else:
        return HttpResponseRedirect("/login/")


@require_http_methods(["GET", "POST"])
def upload(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            return render(request, 'upload/upload.html', {'form': VideoUploadForm()})
        else:
            form = VideoUploadForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                video.status = 4
                video.owner = request.user
                video.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, 'upload/upload.html', {'error': form.errors, 'video': request.POST, 'form': form })
    else:
        return HttpResponseRedirect("/login/")
