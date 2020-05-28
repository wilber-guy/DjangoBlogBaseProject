from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return http responce
    return HttpResponse('<h1>Hello Main Poll</1>')

def about(request):
    return HttpResponse('<h1>About</h1>') 