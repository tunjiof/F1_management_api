from django.urls import path
from .views import DriverViews

urlpatterns = [
    path('driver/', DriverViews.as_view(), name= 'driver'),
    path('driver/<int:id>/', DriverViews.as_view(), name= 'driver_with_params')
]