from levelupapi.models.events import Events
from levelupapi.models.gamer import Gamer
from django.db import models


class EventGamers(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
