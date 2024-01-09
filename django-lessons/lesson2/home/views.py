from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def get_age(request):
    return HttpResponse('21')

def get_info(request):
    return HttpResponse('Mening ismim Shaxriyor\nBuxoroda yashayman!')


class GetInfo(TemplateView):
    template_name = 'index.html'


class GetAge(TemplateView):
    template_name = 'age.html'