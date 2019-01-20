from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlarmsView.as_view()),
    # a/ Alarm endpoint
    path('a/<int:id>', views.AlarmView.as_view())
]
