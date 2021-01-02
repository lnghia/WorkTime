from django.urls import path
from .Views import Login, Home, Logout

app_name = "web"

urlpatterns = [
    path('login/', view=Login.login_account, name='login'),
    path('', view=Home.index, name='home'),
    path('logout/', view=Logout.logout_user, name='logout'),
]