from . import views
from django.urls import path


urlpatterns = [
    path('device/', views.search_device, name='search_device'),
    path('device/<int:device_id>/', views.Device_view, name='device-view'),
]