from django.db import models


class Alarms(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of alarm',
    )
    user = models.CharField(
        max_length=20,
        help_text='User',
    )
    alarm = models.DateTimeField()
