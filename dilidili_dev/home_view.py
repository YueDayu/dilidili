from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import *
from django.contrib import auth
from dilidili_dev.users import User

@require_http_methods(["GET"])
def following(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden()
	else:
		return render(request, "home/follow-list.html",
				  	  context={
				  		'follow_set': request.user.follow_users.all(),
				  		'empty_msg': '你没有关注的人',
				  	  })


@require_http_methods(["GET"])
def follower(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden()
	else:
		return render(request, "home/follow-list.html", 
			          context={
			          	'follow_set': request.user.following_users.all(),
			          	'empty_msg': '还没有关注你的人',
			          })

@require_http_methods(["GET"])
def collection(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden()
	else:
		return render(request, "home/collection-list.html",
					  context={
					  	'video_set': request.user.collection_videos.all().order_by('-time'),
					  	'empty_msg': '你还没有收藏的视频'
					  })


@require_http_methods(["GET"])
def center(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden()
	else:
		return render(request, "home/main-content.html",
			          context={
			          	'home_video_set': request.user.video_set.all().order_by('-time'),
			          	'home_video_collection': request.user.collection_videos.all().order_by('-time')
			          })
