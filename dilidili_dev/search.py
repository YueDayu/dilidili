from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import *


#for ajax GET, return JSON
@require_http_methods(["GET"])
def search(request):
	return JsonResponse(serializers.serialize('json', Video.objects.all()), safe=False)


@require_http_methods(["GET"])
def search_mainpage(request):
	return render(request, 'search/search.html')
