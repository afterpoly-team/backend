from django.shortcuts import render
from .serializers import OnlineEventSerializer, TagSerializer, RealLifeEventSerializer, PlaceSerializer, AddressSerializer
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent
from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .service import OnlineEventFilter, PlaceFilter, RealLifeEventFilter


class OnlineEventViewSet(viewsets.ModelViewSet):
    serializer_class = OnlineEventSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OnlineEventFilter

    queryset = OnlineEvent.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RealLifeEventViewSet(viewsets.ModelViewSet):
    serializer_class = RealLifeEventSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RealLifeEventFilter

    queryset = RealLifeEvent.objects.all()


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlaceFilter

    queryset = Place.objects.all()


class AdressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
