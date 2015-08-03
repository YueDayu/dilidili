from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_http_methods

#for ajax GET, return JSON
@require_http_methods(["GET"])
def search(request):
	pass


@require_http_methods(["GET"])
def search_mainpage(request):
	return render(request, 'search/search.html')
