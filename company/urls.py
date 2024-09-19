"""Company app URL configuration."""

from django.urls import path

from company import views

urlpatterns = [
    path('', views.index, name="home"),
]
