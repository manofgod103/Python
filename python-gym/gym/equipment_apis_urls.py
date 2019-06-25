from django.conf.urls import url

from .equipment_apis import *

urlpatterns = [
    url(r"^create/",EquipmentCreateAPIView.as_view())
]