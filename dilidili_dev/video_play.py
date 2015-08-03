__author__ = 'Yue Dayu'

from django.shortcuts import render
from .models import Video
from django.http import Http404


def video_play(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'video/video.html', {'video': video})
