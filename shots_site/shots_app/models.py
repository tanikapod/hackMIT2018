from django.db import models

class DrinkingGame(models.Model):
    title = models.CharField(max_length = 200)
    #author = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date created')
    play_date = models.DateTimeField('date last played')
    play_count = models.IntegerField(default = 0)

class Trigger(models.Model):
    drinking_game = models.ForeignKey(DrinkingGame, on_delete = models.CASCADE)

    trigger = models.CharField(max_length = 200)

class Action(models.Model):
    trigger = models.ForeignKey(Trigger, on_delete = models.CASCADE)

    amount = models.IntegerField(default = 1)
    description = models.CharField(max_length = 200)
