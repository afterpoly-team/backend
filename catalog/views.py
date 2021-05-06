from django.shortcuts import render
from .serializers import OnlineEventSerializer, TagSerializer, RealLifeEventSerializer, PlaceSerializer, AddressSerializer
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent
from rest_framework import viewsets, pagination, filters
from django_filters.rest_framework import DjangoFilterBackend
from .service import OnlineEventFilter, PlaceFilter, RealLifeEventFilter, LimitPagination
from rest_framework.decorators import api_view
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet


SEARCH_FIELDS_FOR_ALL_TYPES = ('title', 'description', 'short_description', 'organizers', 'additional_information', )

# * ORDERING = ?ordering=field -> упорядочевание


class OnlineEventViewSet(viewsets.ModelViewSet):
    serializer_class = OnlineEventSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = SEARCH_FIELDS_FOR_ALL_TYPES
    filterset_class = OnlineEventFilter

    queryset = OnlineEvent.objects.all().order_by('list_of_dates')


class TagViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RealLifeEventViewSet(viewsets.ModelViewSet):
    serializer_class = RealLifeEventSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = SEARCH_FIELDS_FOR_ALL_TYPES
    filterset_class = RealLifeEventFilter

    queryset = RealLifeEvent.objects.all().order_by('list_of_dates')


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    # * filtering
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = SEARCH_FIELDS_FOR_ALL_TYPES
    filterset_class = PlaceFilter

    queryset = Place.objects.all()


class AdressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AllEventTypesViewSet(ObjectMultipleModelAPIViewSet):

    querylist = [
        {'queryset': OnlineEvent.objects.all().order_by('list_of_dates'), 'serializer_class': OnlineEventSerializer},
        {'queryset': RealLifeEvent.objects.all().order_by('list_of_dates'), 'serializer_class': RealLifeEventSerializer},
        {'queryset': Place.objects.all(), 'serializer_class': PlaceSerializer},
    ]
    pagination_class = LimitPagination
    
    filter_backends = (filters.SearchFilter,)
    search_fields = SEARCH_FIELDS_FOR_ALL_TYPES
