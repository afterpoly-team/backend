from rest_framework import serializers
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent

# * HyperlinkedModelSerializer to be able to go to Tags as links, not as numbers

FILEDS_EVENT_INHERITORS = ['url', 'id', 'title', 'description', 'short_description', 'link',
                           'tags', 'organizers', 'additional_information', 'main_image',
                           'background_image', 'creation_date', ]


class OnlineEventSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="online_event-detail")

    class Meta:
        model = OnlineEvent
        fields = FILEDS_EVENT_INHERITORS + ['list_of_dates', ]


class PlaceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="place-detail")

    class Meta:
        model = Place
        fields = FILEDS_EVENT_INHERITORS + ['address', ]


class RealLifeEventSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="real_life_event-detail")

    class Meta:
        model = RealLifeEvent
        fields = FILEDS_EVENT_INHERITORS + ['address', 'list_of_dates', ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'district', 'region',
                  'street', 'corps', 'house_number', 'index',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', )
