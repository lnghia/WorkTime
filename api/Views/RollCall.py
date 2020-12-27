from api.Models.Worker import Worker
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from ..Constants.Response import make_response
from ..Serializers import RollCallSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def punch_in(request):
    pass


@api_view(['POST'])
def punch_out(request):
    pass


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_roll_call(request):
    try:
        request_data = RollCallSerializer(data=request.data)

        if request_data.is_valid():
            id = request.data['id']
            worker = Worker.objects.get(id=id)
            worker.make_roll_call()

            return JsonResponse(make_response(1, None, None))

        return JsonResponse(make_response(0, None, request_data.errors), status=400)
    except:
        return JsonResponse(make_response(0, None, 'server error'), status=500)
