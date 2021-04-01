from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Trello.models import Task, TaskList

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'AppAuthentication/register.html')


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