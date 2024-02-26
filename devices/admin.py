from django.contrib import admin, messages
from .models import Device, DeviceType, DeviceModel, Parameter


class ParameterInline(admin.StackedInline):
    model = Parameter
    extra = 1


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_type', 'device_model', 'device_add_time']
    list_filter = ['device_type']
    inlines = [ParameterInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "device_model":
            device_type_id = request.POST.get('device_type') or \
                             kwargs.get('initial', {}).get(
                                 'device_type_id')
            if device_type_id:
                kwargs["queryset"] = DeviceModel.objects.filter(device_type_id=device_type_id)
            else:
                kwargs["queryset"] = DeviceModel.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['device_model'].queryset = DeviceModel.objects.filter(device_type=obj.device_type)
        return form

    def message_user(self, request, message, level=messages.INFO, extra_tags='', fail_silently=False):
        message = 'Устройство создано !'
        return super().message_user(request, message, level=level, extra_tags=extra_tags, fail_silently=fail_silently)


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'device_type']
    list_filter = ['device_type']


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['device']


admin.site.register(DeviceType)
