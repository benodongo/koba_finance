from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully login')
            return redirect('home')
        else:
            messages.error(request , 'Invalid user creditials')
            return redirect('index')
    else:

        return render(request, 'accounts/index.html')


def home(request): 
    return render(request, 'accounts/home.html')

def logout(request):
    return redirect('index')