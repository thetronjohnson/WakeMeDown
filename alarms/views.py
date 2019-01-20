from rest_framework import generics

from alarms.models import Alarms
from alarms.serializers import AlarmsSerializer


class AlarmsView(generics.ListCreateAPIView):
    serializer_class = AlarmsSerializer
    queryset = Alarms.objects.all()


class AlarmView(generics.RetrieveDestroyAPIView):
    serializer_class = AlarmsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        alarm = Alarms.objects.filter(id=id)
        return alarm
