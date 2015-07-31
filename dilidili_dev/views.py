from django.shortcuts import render
from django.shortcuts import RequestContext

# Create your views here.

from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from dilidili_dev.admin import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render_to_response("registration/register.html", RequestContext(request))
