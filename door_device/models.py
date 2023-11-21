from django.db import models

class Device(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type
class Door(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    number_door = models.IntegerField()
    status = models.CharField(max_length=255)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self) -> str:
          return f"Nome: {self.name}, IP: {self.ip}, Número: {self.number_door}, Status: {self.status}, Device: {self.device}"