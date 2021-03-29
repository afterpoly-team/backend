from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'title', 'creation_date',
                  'description', 'event_date', 'link', )
