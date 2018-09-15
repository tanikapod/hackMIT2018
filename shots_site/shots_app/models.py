from django.db import models

class DrinkingGame(models.Model):
    title = models.CharField(max_length = 200)
    #author = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date created')
    play_date = models.DateTimeField('date last played')
    play_count = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0,
                                 choices = [(1, 'A anime tittie'),
                                            (2, 'B anime titties'),
                                            (3, 'C anime titties'),
                                            (4, 'D anime titties'),
                                            (5, 'DD anime titties')])

    def __str__(self):
        return self.title

class Trigger(models.Model):
    drinking_game = models.ForeignKey(DrinkingGame, on_delete = models.CASCADE)

    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.description

class Action(models.Model):
    trigger = models.ForeignKey(Trigger, on_delete = models.CASCADE)

    amount = models.IntegerField(default = 1)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.description + str(amount) + "times"
