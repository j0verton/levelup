from django.db import models


class EventGame(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
