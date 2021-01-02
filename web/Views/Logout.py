from django.shortcuts import redirect, render
from ..Forms.LoginForm import LoginForm
from django.contrib.auth import authenticate, logout

def logout_user(request):
    logout(request)
    print(request.user.is_authenticated)
    return redirect('web:login')