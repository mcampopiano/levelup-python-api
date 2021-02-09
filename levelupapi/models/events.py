from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer
from django.db import models


class Events(models.Model):
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    scheduler = models.ForeignKey(Gamer, on_delete=models.CASCADE)