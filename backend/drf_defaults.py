"""
Django rest framework default pagination
"""
from rest_framework.pagination import PageNumberPagination

# * to set page_size must use sth like http://localhost:8000/api/events/?page_size=3


class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100000
