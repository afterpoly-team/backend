from rest_framework import serializers
from .models import Event, Tag


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'title', 'creation_date',
                  'description', 'event_date', 'link', 'tag',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name', )
