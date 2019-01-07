from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychology_test, name="psychology-test"),
]
