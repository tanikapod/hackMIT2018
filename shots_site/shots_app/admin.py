from django.contrib import admin

from .models import DrinkingGame
admin.site.register(DrinkingGame)

from .models import Trigger
admin.site.register(Trigger)

from .models import Action
admin.site.register(Action)
