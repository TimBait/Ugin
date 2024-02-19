from django.db import models
from django.utils import timezone


class DeviceType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(max_length=50)
    devicetype = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=50)
    devicetype = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        return f"Устройство {self.pk}"

