__author__ = 'Yue Dayu'

from django.shortcuts import render
from .models import Video
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Bullet, Comment
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import escape


def video_play(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    if (not request.user.is_authenticated() or not request.user.is_admin) and video.status != 0:
        return render(request, "video/video-notfound.html")
    return render(request, 'video/video.html', {'video': video})


@require_http_methods(['POST'])
def video_bullet_add(request):
    if request.user.is_authenticated() and request.user.can_bullet:
        try:
            video = Video.objects.get(pk=request.POST['id'])
            user = request.user
            time = request.POST['time']
            content = request.POST['content']
            color = request.POST['color']
            b = Bullet(video=video,
                       user=user,
                       time=time,
                       content=content,
                       color=color)
            b.save()
        except Video.DoesNotExist:
            return JsonResponse(data={'res': False,
                                      'error': '发送失败！'})
        return JsonResponse(data={'res': True})
    else:
        return JsonResponse(data={'res': False,
                                  'error': '用户没有权限！'})


@require_http_methods(['POST'])
def video_bullet_get(request):
    try:
        start = float(request.POST['last'])
        video = Video.objects.get(pk=request.POST['id'])
        b_set = Bullet.objects.filter(video=video).order_by("-send_date")
        new_list = []
        max = start
        for x in b_set:
            if x.send_date.timestamp() <= start:
                break
            if x.send_date.timestamp() > max:
                max = x.send_date.timestamp()
            temp = {
                'content': escape(x.content),
                'color': x.color,
                'send_date': str(x.send_date.year) + "-" + str(x.send_date.month) + "-" + str(x.send_date.day),
                'time': x.time
            }
            new_list.append(temp)
        result = {
            'res': True,
            'list': new_list,
            'max': max
        }
        return JsonResponse(data=result)
    except Video.DoesNotExist:
        return JsonResponse(data={'res': False})


@require_http_methods(['POST'])
def video_comment_add(request):
    if request.user.is_authenticated() and request.user.can_comment:
        try:
            video = Video.objects.get(pk=request.POST['id'])
            user = request.user
            content = request.POST['content']
            c = Comment(video=video,
                        user=user,
                        content=content)
            c.save()
        except Video.DoesNotExist:
            return JsonResponse(data={'res': False,
                                      'error': '发送失败！'})
        return JsonResponse(data={'res': True})
    else:
        return JsonResponse(data={'res': False,
                                  'error': '用户没有权限！'})


@require_http_methods(['POST'])
def get_video_comment(request):
    try:
        video = Video.objects.get(pk=request.POST['id'])
        c_set = Comment.objects.filter(video=video).order_by('-time')
        new_list = []
        if not request.user.is_authenticated():
            flag = False
        else:
            flag = True
        for x in c_set:
            thumbnail_url = get_thumbnailer(x.user.image).get_thumbnail({
                'size': (200, 200),
                'box': x.user.cropping,
                'crop': True,
                'detail': True,
            }).url
            if flag:
                if x.user == request.user or request.user.is_admin:
                    flag = True
                else:
                    flag = False
            temp = {
                'user_id': x.user.id,
                'user_name': escape(x.user.name),
                'user_image': thumbnail_url,
                'can_del': flag,
                'comment_id': x.pk,
                'comment_context': escape(x.content),
                'comment_time':
                    str(x.time.month) + '月' + str(x.time.day) + '日 ' + str(x.time.hour) + ':' + str(x.time.minute)
            }
            new_list.append(temp)
        result = {
            'res': True,
            'list': new_list
        }
        return JsonResponse(data=result)
    except Video.DoesNotExist:
        return JsonResponse(data={'res': False})


@require_http_methods(['POST'])
def del_video_comment(request):
    comment_id = int(request.POST['id'])
    if request.user.is_authenticated():
        try:
            comment = Comment.objects.get(pk=comment_id)
            if request.user == comment.user or request.user.is_admin:
                comment.delete()
                return JsonResponse(data={'res': True})
            else:
                return JsonResponse(data={'res': False})
        except Comment.DoesNotExist:
            return JsonResponse(data={'res': False})
    else:
        return JsonResponse(data={'res': False})


@require_http_methods(['POST'])
def set_collection(request):
    if request.user.is_authenticated():
        try:
            video = Video.objects.get(pk=request.POST['id'])
            user = request.user
            if video in user.collection_videos.all():
                flag = False
                user.collection_videos.remove(video)
            else:
                flag = True
                user.collection_videos.add(video)
            return JsonResponse(data={'res': True,
                                      'flag': flag})
        except Video.DoesNotExist:
            return JsonResponse(data={'res': False})
    else:
        return JsonResponse(data={'res': False})


@require_http_methods(['POST'])
def set_like(request):
    if request.user.is_authenticated():
        try:
            video = Video.objects.get(pk=request.POST['id'])
            user = request.user
            if video in user.like_videos.all():
                flag = False
                user.like_videos.remove(video)
            else:
                flag = True
                user.like_videos.add(video)
            return JsonResponse(data={'res': True,
                                      'flag': flag})
        except Video.DoesNotExist:
            return JsonResponse(data={'res': False})
    else:
        return JsonResponse(data={'res': False})


@require_http_methods(['POST'])
def add_money(request):
    if request.user.is_authenticated():
        try:
            video = Video.objects.get(pk=request.POST['id'])
            user = request.user
            if user.money > 0:
                user.money -= 1
                user.save()
                video.money += 1
                money = video.money
                video.save()
                video.owner.money += 1
                video.owner.save()
                return JsonResponse(data={'res': True,
                                          'video_money': money})
            else:
                return JsonResponse(data={'res': False,
                                          'error': "硬币不足"})
        except Video.DoesNotExist:
            return JsonResponse(data={'res': False,
                                      'error': "视频不存在"})
    else:
        return JsonResponse(data={'res': False,
                                  'error': "用户未登录"})
