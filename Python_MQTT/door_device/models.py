from django.db import models

class Doors(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type
class Devices(models.Model):
    ip = models.CharField(max_length=255)
    number_door = models.IntegerField()
    status = models.CharField(max_length=255)
    door = models.ForeignKey(Doors,on_delete=models.CASCADE)


