from django.shortcuts import render
from .serializers import OnlineEventSerializer, TagSerializer
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
