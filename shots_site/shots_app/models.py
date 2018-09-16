import datetime
from django.db import models

class DrinkingGame(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date created', default = datetime.datetime.now())
    play_date = models.DateTimeField('date last played', default = None)
    play_count = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0,
                                 choices = [(1, 'A-cup anime titties'),
                                            (2, 'B-cup anime titties'),
                                            (3, 'C-cup anime titties'),
                                            (4, 'D-cup anime titties'),
                                            (5, 'DD-cup anime titties')])
    def __str__(self):
        return self.title

    @staticmethod
    def get_by_id(id):
        return DrinkingGame.objects.get(id = id)

    def get_triggers_and_actions(self):
        return Trigger.objects.filter(drinking_game = self.id)

class Trigger(models.Model):
    drinking_game = models.ForeignKey(DrinkingGame, on_delete = models.CASCADE)

    trigger = models.CharField(max_length = 200)
    action = models.CharField(max_length = 200)
    amount = models.IntegerField(default = 1)

    def __str__(self):
        return 'when ' + self.trigger + ', do ' + self.action + ' ' + str(self.amount) + ' times'

    @staticmethod
    def get_by_id(id):
        return Trigger.objects.get(id = id)
