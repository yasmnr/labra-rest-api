from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"persons", views.PersonViewSet)
router.register(r"relationships", views.RelationshipViewSet)


urlpatterns = [
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]
