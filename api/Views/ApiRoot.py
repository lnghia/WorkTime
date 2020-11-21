from django.http import response
from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def index(request):
    return Response({'msg': 'testing'})


@api_view(['GET'])
def api_root(request):
    data = {
        'index': 'https://worktime-management.herokuapp.com/api/',
    }

    return Response(data)
