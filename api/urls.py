from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"questions", views.QuestionViewSet)
router.register(r"choices", views.ChoiceViewSet)


urlpatterns = [
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]
