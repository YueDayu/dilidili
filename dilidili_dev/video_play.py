__author__ = 'Yue Dayu'

from django.shortcuts import render


def video_play(request, video_id):
    return render(request, 'video/video.html')