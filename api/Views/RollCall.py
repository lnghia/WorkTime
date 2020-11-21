from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from ..Constants.Response import make_response

@api_view(['POST'])
def punch_in(request):
    pass

@api_view(['POST'])
def punch_out(request):
    pass