from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landingpage(request):
    return HttpResponse("<h2 style='color:red;'>Hellooo</h2><p style='color:navy;'>Picture<p><img src=https://i.pinimg.com/736x/37/94/c2/3794c219ec7dc5ec42c315f401e14db6.jpg>")