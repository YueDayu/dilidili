__author__ = 'Yue Dayu'

from django.shortcuts import render
from .models import Video
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Bullet
from django.core import serializers


def video_play(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("User does not exist")
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
                'content': x.content,
                'color': x.color,
                'send_date': str(x.send_date.month) + "-" + str(x.send_date.day),
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
