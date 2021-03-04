from django.db import models
# from django.contrib.auth.models import User


class Game(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    numberOfPlayers = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
