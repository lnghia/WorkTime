from django.urls import path
from .Views import api_root, index, register_worker

urlpatterns = [
    path('', view=index, name='api-index'),
    path('api_root/', view=api_root, name='api-root'),
    path('new_user/', view=register_worker, name='register-worker'),
]