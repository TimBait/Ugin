from django.db import models
from django.core.validators import  RegexValidator

class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    on_the_network = models.BooleanField()
    ip_address = models.GenericIPAddressField()
    serial_number = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=17,
                                   validators=[RegexValidator(regex=r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$')])

    def __str__(self):
        return f"IP: {self.ip_address}, Serial: {self.serial_number}, MAC: {self.mac_address}"


class Device(models.Model):
    device_add_time = models.DateTimeField(auto_now_add=True, editable=False)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    #parametres = models.OneToOneField(Parameter, on_delete=models.CASCADE)    #вот тут беда

    def __str__(self):
        return str(self.pk)





