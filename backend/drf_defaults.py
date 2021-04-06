"""
Django rest framework default pagination
"""
from rest_framework.pagination import PageNumberPagination

# * to set page_size must use sth like http://localhost:8000/api/events/?page_size=3


class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100000

    def get_paginated_response(self, data):
        response = super(DefaultResultsSetPagination,
                         self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response
