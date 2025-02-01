from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_pagianted_response(self, data):
        return Response(
            
        )