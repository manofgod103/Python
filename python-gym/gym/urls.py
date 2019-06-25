from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^login", UserViewSet.as_view({"post":"login"}))
]