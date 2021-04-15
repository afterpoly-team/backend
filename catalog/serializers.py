from rest_framework import serializers
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent


class OnlineEventSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="online_event-detail")

    class Meta:
        model = OnlineEvent
        fields = ('title', 'description', 'short_description', 'link',
                  'tag', 'organizers', 'additional_information', 'main_image',
                  'background_image', 'creation_date', )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name', )
