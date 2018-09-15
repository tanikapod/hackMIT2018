from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import *

# template = loader.get_template('shots_app/index.html')

def home(request):
    latest_games = DrinkingGame.objects.order_by('-pub_date')[:5]

    most_played = DrinkingGame.objects.order_by('-play_count')[:5]

    top_rated = DrinkingGame.objects.order_by('-rating')[:5]

    context = { 'latest_games' : latest_games,
                'most_played' : most_played,
                'top_rated' : top_rated }
    return render(request, 'shots_app/home.html', context)
    #return HttpResponse(template.render(context, request))

#def makeDrinkingGame(title, triggers):

def create(request):

    return HttpResponse("Create Page")

def play(request):
    return HttpResponse("Play Page")
