from django_filters import rest_framework as filters
from .models import OnlineEvent, Place, RealLifeEvent
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class OnlineEventFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = OnlineEvent
        fields = ['tags', ]


class PlaceFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = Place
        fields = ['tags', ]


class RealLifeEventFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = RealLifeEvent
        fields = ['tags', ]


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 15
