from rest_framework import serializers
from .models import Device, DeviceType, Parameter, DeviceModel


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('id', None)
        return {key: value for key, value in data.items() if value is not None}


class DeviceSerializer(serializers.ModelSerializer):
    device_type = serializers.CharField(source='device_type.name')
    device_model = serializers.CharField(source='device_model.name')
    parameters = ParameterSerializer(source='parameter', many=False)

    class Meta:
        model = Device
        fields = ['id', 'device_add_time', 'device_type', 'device_model', 'parameters']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('device', None)
        data.pop('id', None)
        return {key: value for key, value in data.items() if value is not None}


class DeviceModelSerializer(serializers.ModelSerializer):
    device_type = serializers.CharField(source='device_type.name')

    class Meta:
        model = DeviceModel
        fields = '__all__'


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ['id', 'name']
