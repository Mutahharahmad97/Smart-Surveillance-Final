from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_UR, name="detect_UR")
]
