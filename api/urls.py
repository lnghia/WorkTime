from django.urls import path
from .views import index, api_root

urlpatterns = [
    path('', view=index, name='api-index'),
    path('api_root/', view=api_root, name='api-root'),
]