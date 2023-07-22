from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

   
def firstview(request):
    return HttpResponse('This my first appview')

def anju(request):
    return HttpResponse('hello anju')




