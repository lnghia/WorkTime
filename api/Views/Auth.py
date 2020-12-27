from os import name
from rest_framework.decorators import api_view, permission_classes
from ..Serializers import WorkerSerializer, LoginSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from ..Constants.Response import response, make_response
from ..models import Worker
from ..Util.User_Util import new_user
from ..Util.Email_Util import send_email
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from rest_framework.authtoken.models import Token
import sys


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@permission_required('api.add_worker')
def register_worker(request):
    email = request.data.get('email')
    if email is not None:
        if Worker.objects.filter(email=email).exists():
            worker = Worker.objects.get(email=email)
            return JsonResponse(make_response(1, {'id': worker.id}, None))
    
    try:
        request_data = WorkerSerializer(data=request.data)

        if request_data.is_valid():
            name = request_data['name'].value
            email = request_data['email'].value

            username, password, new_user = Worker.create_account(email)
            new_worker = Worker.objects.create(
                name=name, email=email, user=new_user)
            send_email('Account Initiated', email, 'mail/account_information',
                       {'username': email, 'password': password})
            return JsonResponse(make_response(1, {'id': new_worker.id}, None))
        return JsonResponse(make_response(0, None, request_data.errors), status=400)
    except:
        # print(sys.exc_info()[0])
        return JsonResponse(make_response(0, None, 'server error'), status=500)


@api_view(['POST'])
def login(request):
    try:
        request_data = LoginSerializer(data=request.data)

        if request_data.is_valid():
            try:
                worker = Worker.objects.get(email=request.data['username'])
                if worker.verify_password(request.data['password']):
                    token = worker.generate_token()
                    return JsonResponse(make_response(1, {'token': str(token)}, None))
                # print(sys.exc_info()[0])
                return JsonResponse(make_response(0, None, 'invalid username or password'), status=404)
            except:
                # print(sys.exc_info()[0])
                return JsonResponse(make_response(0, None, 'invalid username or password'), status=404)
        return JsonResponse(make_response(0, None, request_data.errors), status=400)
    except:
        return JsonResponse(make_response(0, None, 'server error'), status=500)
