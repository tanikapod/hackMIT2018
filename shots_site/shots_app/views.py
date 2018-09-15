from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    latest_games = DrinkingGame.objects.order_by('-pub_date')[:5]
    latest = 'Games Recently Created:\n' + ', '.join([g.title for g in latest_games])

    most_played = DrinkingGame.objects.order_by('-play_count')[:5]
    popular = '\nMost Popular Games:\n' + ', '.join([g.title for g in most_played])

    top_rated = DrinkingGame.objects.order_by('-rating')[:5]
    rat = '\nTop Rated:\n' + ', '.join([g.title for g in top_rated])

    return HttpResponse(latest, popular, rat)

def create(request):
    return HttpResponse("Create Page")

def play(request):
    return HttpResponse("Play Page")
