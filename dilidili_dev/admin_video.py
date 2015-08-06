from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import Video
from django.contrib import auth
from dilidili_dev.users import User


@require_http_methods(["GET"])
def remove(request, video_id):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return Http404("Video not found")
    if request.user.pk != video.owner.pk:
        return HttpResponseForbidden()
    else:
        video.delete()
        return HttpResponseRedirect("/home/")


@require_http_methods(["POST"])
def togglepublish(request, video_id):
    if not request.user.is_authenticated() or not request.user.is_admin:
        return HttpResponseForbidden()
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return Http404("Video not found")
    video.status = 0 if video.status != 0 else 2
    video.save()
    return HttpResponse()
