from django.urls import path
from .views import TeamViews

urlpatterns = [
    path('team/', TeamViews.as_view(), name= 'team'),
    path('team/<int:id>/', TeamViews.as_view(), name= 'team')
]