from .models import Device, Parameter

def get_device_parameters(device_id):        #получаем id параметра по device_id
    try:
        device = Device.objects.get(pk=device_id)
        parameters = Parameter.objects.filter(device=device)
        return parameters
    except Device.DoesNotExist:
        return None



