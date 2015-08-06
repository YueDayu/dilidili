from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponseBadRequest, QueryDict
from django.views.decorators.http import require_http_methods
from dilidili_dev.models import *


def get_search_objects(request):
    data = request.GET.copy()
    sortby = data.pop("order_by")[0] if "order_by" in data else "?"
    offset = int(data.pop("offset")[0] if "offset" in data else "0")
    limitto = int(data.pop("limit_to")[0] if "limit_to" in data else "100")
    objects = Video.objects.all().filter(**data.dict()).order_by(sortby)[offset: offset + limitto]
    return objects


# for ajax GET, return JSON
@require_http_methods(["GET"])
def search(request):
    return JsonResponse(serializers.serialize('json', get_search_objects(request)), safe=False)


@require_http_methods(["GET"])
def search_mainpage(request):
    return render(request, 'search/search.html',
                  context={'category_set': Category.objects.all(), 'title_contain': request.GET["title_include"]})


@require_http_methods(["GET"])
def search_html(request):
    return render(request, "search/search-result.html",
                  context={'video_set': get_search_objects(request)})
