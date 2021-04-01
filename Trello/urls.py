from django.urls import path
from Trello import views

urlpatterns = [
    path('Trello/create_task', views.createTask, name="newTask"),
    path('Trello/create_tasklist', views.createList, name="newTaskList"),
    path('Trello/index', views.index, name="index"),
]