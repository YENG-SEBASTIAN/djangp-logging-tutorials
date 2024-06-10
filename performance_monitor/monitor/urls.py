from django.urls import path

from monitor import views

urlpatterns = [
    path('', views.example_view, name="home"),
]