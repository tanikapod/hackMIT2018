from django.contrib import admin
from .models import DrinkingGame
from .models import Trigger
from .models import Action

admin.site.register(DrinkingGame)
admin.site.register(Trigger)
admin.site.register(Action)
