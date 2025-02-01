from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import Response


class CustomPagination(PageNumberPagination):
    def get_pagianted_response(self, data):
        return Response(

        )