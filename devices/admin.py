from django.contrib import admin
from .models import DeviceType, DeviceModel, Parameter, Device

admin.site.register(DeviceType)
admin.site.register(DeviceModel)
admin.site.register(Parameter)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    filter_horizontal = ('parameters',)