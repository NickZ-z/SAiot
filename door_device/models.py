from django.db import models

class Device(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type
class Door(models.Model):
    name = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255, null=True)
    number_door = models.IntegerField(null=True)
    status = models.CharField(max_length=255, null=True)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self) -> str:
          return f"Nome: {self.name}, IP: {self.ip}, Número: {self.number_door}, Status: {self.status}, Device: {self.device}"