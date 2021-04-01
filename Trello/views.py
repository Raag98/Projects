from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TaskList
from .forms import TaskForm, TaskListForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    lists = TaskList.objects.all()
    return render(request, 'Trello/index.html', {'lists' : lists})

@login_required(login_url='login')
def createList(request):
    if(request.method == 'POST'):
        list = TaskListForm(data = request.POST)
        list.instance.user = request.user
        if list.is_valid():
            list.save()
            return redirect('dashboard')
    else:
        list = TaskListForm()
    
    return render(request, 'Trello/createTaskList.html', {'list' : list})

@login_required(login_url='login')
def createTask(request):
    if(request.method == 'POST'):
        form = TaskForm(data = request.POST)
        # form.instance.list = request.list
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    
    return render(request, 'Trello/createTask.html', {'form' : form})