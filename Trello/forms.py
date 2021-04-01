from django import forms
from .models import Task, TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'desc', 'dueDate', 'list']
        widgets = {
            'dueDate' : forms.DateTimeInput(attrs={'type' : 'datetime-local'})
        }


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name'] 