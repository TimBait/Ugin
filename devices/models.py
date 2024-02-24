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


class Device(models.Model):
    device_add_time = models.DateTimeField(auto_now_add=True, editable=False)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Parameter(models.Model):
    DEVICE_ROLE_CHOICES = (
        ('KV','Квартальный' ),
        ('SB_KL', 'Субкольцевой'),
        ('KL', 'Кольцевой'),
        ('VK', 'Вход в квартал'),
        ('P_VK', 'Идеальный ВК'),
    )
    PORT_NUMBERS_CHOICES = (
        ('8', '8'),
        ('12', '12'),
        ('24', '24'),
        ('48', '48')
    )
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    on_the_network = models.BooleanField()
    ip_address = models.GenericIPAddressField(unique=True)
    serial_number = models.CharField(max_length=20, unique=True)
    mac_address = models.CharField(max_length=17, unique=True,
                                   validators=[RegexValidator(regex=r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$')])
    device_role = models.CharField(max_length=20, choices=DEVICE_ROLE_CHOICES)
    port_numbers = models.CharField(max_length=4, choices=PORT_NUMBERS_CHOICES)
    

    def __str__(self):
        return str(self.pk)




