from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import *
from django.contrib import auth
from dilidili_dev.users import User


@require_http_methods(["POST"])
def toggle_user_upload(request, user_id):
    if not request.user.is_authenticated() or not request.user.is_admin:
        return HttpResponseForbidden()
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        user.can_upload = not user.can_upload
        user.save()
        return HttpResponse()


@require_http_methods(["POST"])
def toggle_user_comment(request, user_id):
    if not request.user.is_authenticated() or not request.user.is_admin:
        return HttpResponseForbidden()
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        user.can_comment = not user.can_comment
        user.save()
        return HttpResponse()


@require_http_methods(["POST"])
def toggle_user_bullet(request, user_id):
    if not request.user.is_authenticated() or not request.user.is_admin:
        return HttpResponseForbidden()
    else:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        user.can_bullet = not user.can_bullet
        user.save()
        return HttpResponse()
