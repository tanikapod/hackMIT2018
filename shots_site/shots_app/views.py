from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    latest_games = DrinkingGame.objects.order_by('-pub_date')[:5]

    most_played = DrinkingGame.objects.order_by('-play_count')[:5]

    top_rated = DrinkingGame.objects.order_by('-rating')[:5]

    context = { 'latest_games' : latest_games,
                'most_played' : most_played,
                'top_rated' : top_rated }
    return render(request, 'shots_app/home.html', context)

'''
triggers_and_actions_with_amounts - dictionary, maps
trigger : (action, amount)

returns id of game created
'''
def make_drinking_game(title, triggers_and_actions_with_amounts):
    new_game = DrinkingGame(title = title)
    new_game.save()
    for (t, (a, num)) in triggers_and_actions_with_amounts.items():
        new_trigger = Trigger(drinking_game = new_game.id, description = t)
        new_trigger.save()
        new_action = Action(trigger = t.id, amount = num, description = a)
        new_action.save()
    return new_game.id

def create(request):
    context = { 'make_drinking_game' : make_drinking_game }
    return render(request, 'shots_app/create.html', context)

def game_detail(request, game_id):
    game = DrinkingGame.get_by_id(game_id)
    triggers_with_actions = game.get_triggers_and_actions()
    context = { 'game' : game,
                'triggers_with_actions' : triggers_with_actions,
                'range' : range(len(triggers_with_actions))}
    return render(request, 'shots_app/game_detail.html', context)

def play(request):
    return HttpResponse("Play Page")
