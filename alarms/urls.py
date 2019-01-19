from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlarmsView.as_view()),
]
