from django.shortcuts import render
from .serializers import EventSerializer, TagSerializer
from .models import Event, Tag
from rest_framework import viewsets, pagination

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
