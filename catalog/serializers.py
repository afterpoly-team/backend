from rest_framework import serializers
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent


class OnlineEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OnlineEvent
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name', )
