from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says what's up bae? <br><br> Go to the <a href='/rango/about'>about</a> page.")

def about(request):
    return HttpResponse("This is the about page! <br><br> Back to the <a href='/rango/'>home</a> page.")
