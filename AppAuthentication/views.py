from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from Trello.models import Task, TaskList

# Create your views here.

@csrf_exempt
def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        authLogin(request, user)
        return redirect('login')
    return render(request, 'AppAuthentication/register.html', {'form': form})


def dashboard(request):
    user = request.user
    lists = TaskList.objects.filter(user=user)
    tasks = Task.objects.filter(list__in=lists)
    return render(request, 'AppAuthentication/dashboard.html', {'lists':lists, 'tasks':tasks})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authLogin(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username / Password is Incorrect')        
    return render(request, 'AppAuthentication/login.html')



def logout(request):
    authLogout(request)
    return redirect('home')


def home(request):
    return render(request, 'AppAuthentication/home.html')