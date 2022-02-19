from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def FirstHomePage(request):
    return HttpResponse('Homepage')
