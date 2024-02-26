from .models import Device, DeviceType, DeviceModel
from django.shortcuts import render, get_object_or_404
from .utils import get_device_parameters
from devices.serializers import DeviceSerializer, DeviceModelSerializer, DeviceTypeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


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

def search_device(request):           #представление для формы поиска device
    if 'device_id' in request.GET:
        device_id = request.GET['device_id']
        try:
            device = Device.objects.get(pk=device_id)
            parameters = get_device_parameters(device_id)
            return render(request, 'devices/device.html', {'device': device,
                                                           'parameters': parameters})
        except Device.DoesNotExist:
            return render(request, 'device_not_found.html')
    else:
        devices = Device.objects.all()
        return render(request, 'devices/search_device.html', {'devices': devices})



class DeviceListView(APIView):
    def get(self, request, format=None):
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeviceAPIView(APIView):
    def get(self, request, device_id):
        try:
            device = Device.objects.get(pk=device_id)
            serializer = DeviceSerializer(device)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)


class DeviceModelListView(APIView):
    def get(self, request, format=None):
        queryset = DeviceModel.objects.all()
        serializer = DeviceModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeviceTypeListView(APIView):
    def get(self, request, format=None):
        queryset = DeviceType.objects.all()
        serializer = DeviceTypeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


