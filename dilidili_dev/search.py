from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponseBadRequest, QueryDict
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import *


#for ajax GET, return JSON
@require_http_methods(["GET"])
def search(request):
	data = request.GET
	objects = Video.objects.all()
	if "filters" in data:
		filters_tmp = QueryDict(data["filters"])
		for field in filters_tmp:
			field_new = field if "__" in field else field + "__iexact"
			objects = objects.filter(**{field_new:filters_tmp.get(field)})
	sortby = data["order_by"] if "sortby" in data else "?"
	offset = int(data["offset"] if "offset" in data else "0")
	limitto = int(data["limit_to"] if "limit_to" in data else "100")
	objects = objects.order_by(sortby)[offset : offset+limitto]
	return JsonResponse(serializers.serialize('json', objects), safe=False)


@require_http_methods(["GET"])
def search_mainpage(request):
	return render(request, 'search/search.html')
