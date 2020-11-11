from django.urls import path, urls
from .views import index

urlpatterns = [
    path('/', view=index, name='api-index'),
]