from django.http import response
from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(http_method_names=['GET'])
def index(request):
    return Response({'msg': 'testing'})