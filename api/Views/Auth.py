from os import name
from rest_framework.decorators import api_view
from ..Serializers import WorkerSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from ..Constants.Response import response, make_response
from ..Models.Worker import Worker
from ..Util.User_Util import new_user
from ..Util.Email_Util import send_email


@api_view(['POST'])
def register_worker(request):
    try:
        request_data = WorkerSerializer(data=request.data)

        if request_data.is_valid():
            name = request_data['name'].value
            email = request_data['email'].value

            username, password, new_user = Worker.create_account(email)
            new_worker = Worker.objects.create(name=name, email=email, user=new_user)
            send_email('Account Initiated', email, {'username': username,
                                                    'password': password})
            return JsonResponse(make_response(1,{'id': new_worker.id}, None))
        return JsonResponse(make_response(0, None, request_data.errors))
    except:
        return JsonResponse(make_response(0, None, 'server error'))