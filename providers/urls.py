from django.urls import path, include
from rest_framework import routers

from providers.views import ProviderList


urlpatterns = [
    path('', ProviderList.as_view(), name='ProviderList'),
]
