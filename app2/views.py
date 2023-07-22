from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def secondview(request):
    return HttpResponse('<marquee>this is my second appv2iew</marquee>')

def hello(request):
    return HttpResponse('<marquee>HELLO WORLD</marquee>')


