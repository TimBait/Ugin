from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class DeviceType(models.Model):
    PARAM_SET = (
        ('1', 'Switch'),
        ('2', 'Cam'),
        ('3', 'Wifi'),
    )
    name = models.CharField(max_length=25)
    parameter_settings = models.CharField(max_length=15, choices=PARAM_SET)

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
        ('KV', 'Квартальный'),
        ('SUBKL', 'Субкольцевой'),
        ('KL', 'Кольцевой'),
        ('VK', 'Вход в квартал'),
        ('PVK', 'Идеальный ВК'),
    )
    PORT_NUMBERS_CHOICES = (
        ('8', '8'),
        ('12', '12'),
        ('24', '24'),
        ('48', '48')
    )
    VIEW_ANGLE_CHOICES = (
        ('100', '100'),
        ('90', '90'),
        ('75', '75'),
        ('60', '60'),
    )
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    on_the_network = models.BooleanField()
    ip_address = models.GenericIPAddressField(unique=True)
    serial_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    mac_address = models.CharField(max_length=17, null=True, blank=True, unique=True,
                                   validators=[RegexValidator(regex=r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$')])
    device_role = models.CharField(max_length=20, null=True, blank=True, choices=DEVICE_ROLE_CHOICES)
    port_numbers = models.CharField(max_length=4, null=True, blank=True, choices=PORT_NUMBERS_CHOICES)
    cam_number = models.CharField(max_length=16, null=True, blank=True)
    micro = models.BooleanField(null=True, blank=True)
    view_angle = models.CharField(null=True, blank=True, max_length=5, choices=VIEW_ANGLE_CHOICES)
    azimuth = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    antenna_height = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return str(self.pk)
