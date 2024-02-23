from django.db import models
from datetime import datetime

class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_add_time = models.DateTimeField(auto_now_add=True, editable=False)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)





