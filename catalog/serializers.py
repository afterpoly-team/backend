from rest_framework import serializers
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent

# * HyperlinkedModelSerializer to be able to go to Tags as links, not as numbers

# event_fields = ('url', 'id', 'title', 'description', 'short_description', 'link',
#                 'tag', 'organizers', 'list_of_dates', 'additional_information', 'main_image',
#                 'background_image', 'creation_date', )


class OnlineEventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="online_event-detail")

    class Meta:
        model = OnlineEvent
        fields = ('url', 'id', 'title', 'description', 'short_description', 'link',
                  'tag', 'organizers', 'list_of_dates', 'additional_information', 'main_image',
                  'background_image', 'creation_date', )


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="place-detail")

    class Meta:
        model = Place
        fields = ('url', 'id', 'title', 'description', 'short_description', 'link',
                  'tag', 'organizers', 'additional_information', 'main_image',
                  'background_image', 'creation_date', 'address', )


class RealLifeEventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="real_life_event-detail")

    class Meta:
        model = RealLifeEvent
        fields = ('url', 'id', 'title', 'description', 'short_description', 'link',
                  'tag', 'organizers', 'list_of_dates', 'additional_information', 'main_image',
                  'background_image', 'creation_date', 'address', )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'district', 'region',
                  'street', 'corps', 'house_number', 'index',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name', )
