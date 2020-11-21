from api.Models.Worker import Worker
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from ..Constants.Response import make_response
from ..Serializers import RollCallSerializer


@api_view(['POST'])
def punch_in(request):
    pass


@api_view(['POST'])
def punch_out(request):
    pass


@api_view(['POST'])
def make_roll_call(request):
    try:
        request_data = RollCallSerializer(data=request.data)

        if request_data.is_valid():
            id = request.data['id']
            worker = Worker.objects.get(id=id)
            worker.make_roll_call()

            return JsonResponse(make_response(1, None, None))

        return JsonResponse(make_response(0, None, request_data.errors))
    except:
        return JsonResponse(make_response(0, None, 'server error'))
