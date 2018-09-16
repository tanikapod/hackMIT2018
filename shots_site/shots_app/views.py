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
def make_drinking_game(request):
    title = request.POST['title']
    triggers = [(request.POST['trigger'],
                request.POST['action'],
                request.POST['action_amount'])]

    game = DrinkingGame(title = title)
    game.save()
    triggers = []
    for (trigger, action, amount) in triggers:
        new_trigger = Trigger(drinking_game = game, trigger = trigger, action = action, amount = amount)
        triggers.append(new_trigger)
        new_trigger.save()
        print(Trigger.objects)
    print(triggers)
    context = { 'game' : game,
                'triggers' : triggers}
    return render(request, 'shots_app/game_detail.html', context)

def create(request):
    context = { 'make_drinking_game' : make_drinking_game }
    return render(request, 'shots_app/create.html', context)

def game_detail(request, game_id):
    game = DrinkingGame.get_by_id(game_id)
    triggers = game.get_triggers()
    context = { 'game' : game,
                'triggers' : triggers }
    return render(request, 'shots_app/game_detail.html', context)

def play(request):
    return HttpResponse("Play Page")
