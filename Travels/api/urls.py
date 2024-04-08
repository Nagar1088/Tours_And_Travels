from django.contrib import admin
from django.urls import path,include
from api.views import DestinationViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'Destination',DestinationViewset)

urlpatterns = [
    path('',include(router.urls)),
]