from django.urls import path
from .Views import Login, Home

app_name = "web"

urlpatterns = [
    path('login/', view=Login.login_account, name='login'),
    path('', view=Home.index, name='home'),
]