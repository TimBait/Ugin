from . import views
from django.urls import path
from .views import DeviceListView, DeviceAPIView, DeviceModelListView, DeviceTypeListView

urlpatterns = [
    path('device/', views.search_device, name='search_device'),  #форма ввода id Device
    path('device/<int:device_id>/', views.Device_view, name='device-view'),   #форма просмотра Device
    path('api_devices/', DeviceListView.as_view(), name='product-list'), #get на все
    path('api_device/<int:device_id>/', DeviceAPIView.as_view(), name='device_api'), #get по id device
    path('api_device_models/', DeviceModelListView.as_view(), name='device_model_api'), #get всех моделей
    path('api_device_types/', DeviceTypeListView.as_view(), name='device_model_api'), #get всех типов
]