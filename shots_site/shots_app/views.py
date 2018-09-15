from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def create(request):
    return HttpResponse("Create Page")

def play(request):
    return HttpResponse("Play Page")
