from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    etage = models.IntegerField()
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.name} : salle n°{self.numero} au {self.etage} étage"


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} à {self.start_time} le {self.date}"
