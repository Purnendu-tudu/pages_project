import imp
from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class homePageView(TemplateView):
    template_name = 'home.html'


class aboutPageView(TemplateView):
    template_name = 'about.html'

class roboPageView(TemplateView):
    template_name = 'robo.html'