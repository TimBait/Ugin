from .models import Device, DeviceType, DeviceModel
from django.shortcuts import render, get_object_or_404
from .utils import get_device_parameters
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


def Device_view(request):
    device_id = request.GET.get('device_id')
    if device_id:
        try:
            device = get_object_or_404(Device, pk=device_id)
            parameters = get_device_parameters(device)
            return render(request, 'devices/device.html', {'device': device,
                                                           'parameters': parameters})
        except Device.DoesNotExist:
            return render(request, 'device_not_found.html')
    else:
        return render(request, 'search_device.html')

def search_device(request):
    if 'device_id' in request.GET:
        device_id = request.GET['device_id']
        try:
            device = Device.objects.get(pk=device_id)
            parameters = get_device_parameters(device_id)  # Получаем параметры устройства
            return render(request, 'devices/device.html', {'device': device, 'parameters': parameters})
        except Device.DoesNotExist:
            return render(request, 'device_not_found.html')
    else:
        devices = Device.objects.all()
        return render(request, 'devices/search_device.html', {'devices': devices})




