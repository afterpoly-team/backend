from django.shortcuts import render
from .serializers import OnlineEventSerializer, TagSerializer, RealLifeEventSerializer, PlaceSerializer, AddressSerializer
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent
from rest_framework import viewsets, pagination

# Create your views here.


class OnlineEventViewSet(viewsets.ModelViewSet):
    serializer_class = OnlineEventSerializer
    queryset = OnlineEvent.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RealLifeEventViewSet(viewsets.ModelViewSet):
    serializer_class = RealLifeEventSerializer
    queryset = RealLifeEvent.objects.all()


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class AdressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
