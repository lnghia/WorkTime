import json
from api.models.Worker import Worker
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from ..Constants.Response import make_response
from ..Serializers import RollCallSerializer
from rest_framework.permissions import IsAuthenticated
from ..Serializers.Identify import *
import requests

url = 'http://127.0.0.1:5000/api/'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_photos(request):
    try:
        data = SubmitPhotoSerializer(data=request.data)
        if data.is_valid():
            response = requests.post(url+'submit-photos/', json=request.data)
            if response.json()['is_success']:
                return JsonResponse(make_response(1, None, None))
            else:
                return JsonResponse(make_response(0, None, 'server error'), status=500)
        return JsonResponse(make_response(0, None, data.errors), status=400)
    except:
        return JsonResponse(make_response(0, None, 'server error'), status=500)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict_photo(request):
    try:
        data = PredictPhotoSerializer(data=request.data)

        if data.is_valid():
            response = requests.post(url+'identify-photo/', json=request.data)
            id = int(response.json()['data']['id'])
            if response.json()['is_success']:
                print(f'{id} - {type(id)} - {Worker.objects.filter(id=id).exists()}')
                if Worker.objects.filter(id=id).exists():
                    name = Worker.objects.get(id=id).name
                    return JsonResponse(make_response(1, {'id': id, 'name': name}, None))
                return JsonResponse(make_response(0, None, 'server error'), status=500)
            else:
                return JsonResponse(make_response(0, None, 'server error'), status=500)
        return JsonResponse(make_response(0, None, data.errors), status=400)
    except:
        return JsonResponse(make_response(0, None, 'server error'), status=500)
