from django.contrib import admin
from .models import Device, DeviceType, DeviceModel, Parameter
from django.utils.translation import gettext as _
from django.contrib import messages

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'device_model', 'device_add_time')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "device_model":
            device_type_id = request.POST.get('device_type') or \
                             kwargs.get('initial', {}).get('device_type_id')  # Получаем device_type_id из начальных данных
            if device_type_id:
                kwargs["queryset"] = DeviceModel.objects.filter(device_type_id=device_type_id)
            else:
                kwargs["queryset"] = DeviceModel.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Если устройство уже существует (редактирование)
            form.base_fields['device_model'].queryset = DeviceModel.objects.filter(device_type=obj.device_type)
        return form

    def message_user(self, request, message, level=messages.INFO, extra_tags='', fail_silently=False):
        message = _('Устройство создано !')
        return super().message_user(request, message, level=level, extra_tags=extra_tags, fail_silently=fail_silently)


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType)
admin.site.register(DeviceModel)
admin.site.register(Parameter)