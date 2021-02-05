from levelupapi.models.GameTypes import GameTypes
from levelupapi.models.gamer import Gamer
from django.db import models


class Games(models.Model):

    title = models.CharField(max_length=25)
    game_type = models.ForeignKey(GameTypes, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)