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

#def make_drinking_game(title, triggers):

def create(request):
    context = { 'make_drinking_game' : make_drinking_game }
    return render(request, 'shots_app/create.html', context)

def game_detail(request, game_id):
    context = { 'game' : DrinkingGame.get_by_id(game_id) }
    return render(request, 'shots_app/game_detail.html', context)

def play(request):
    return HttpResponse("Play Page")
