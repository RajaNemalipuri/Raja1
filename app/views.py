from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def firstview(request):
    return HttpResponse('Hii world How are you')