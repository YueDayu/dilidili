__author__ = 'Yue Dayu'
from django.shortcuts import render
from .forms import ImageForm
from django.views.decorators.http import require_http_methods


def upload_photo(request):
    return render(request, 'forms/upload-photo.html')


@require_http_methods(["POST"])
def process_img(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user.image = form.files['image']
            user.save()
            form = ImageForm(instance=user)
            return render(request, 'forms/process-photo.html', {'form': form})


@require_http_methods(["POST"])
def upload_success(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            form = ImageForm(request.POST, instance=user)
            form.save()
            return render(request, 'forms/upload-success.html')
