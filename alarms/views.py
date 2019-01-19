from rest_framework import generics

from alarms.models import Alarms
from alarms.serializers import AlarmsSerializer


class AlarmsView(generics.ListCreateAPIView):
    serializer_class = AlarmsSerializer
    queryset = Alarms.objects.all()
