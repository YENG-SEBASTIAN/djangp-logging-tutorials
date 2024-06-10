from django.urls import path

from monitor import views

urlpatterns = [
    path('', views.home, name="home"),
]