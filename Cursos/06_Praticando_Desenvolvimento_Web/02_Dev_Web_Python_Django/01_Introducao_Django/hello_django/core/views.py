from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome):
    return HttpResponse('<h1>Hello World ! by: {}</h1>'.format(nome))