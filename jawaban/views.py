from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landingpage(request):
    return HttpResponse("Hello, Ini Halaman Saya.")