from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def home_view(request):
    return HttpResponse('Hello, World!')

class home_view(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


# Create your views here.

