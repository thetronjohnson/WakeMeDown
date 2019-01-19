from rest_framework import serializers

from alarms.models import Alarms


class AlarmsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Alarms
        fields = '__all__'
