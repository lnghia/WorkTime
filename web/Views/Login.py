from django.shortcuts import redirect, render
from ..Forms.LoginForm import LoginForm
from django.contrib.auth import authenticate, login

def login_account(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(1)
            return redirect('web:home')

    form = LoginForm()

    return render(request, 'html/login.html', {'form': form})