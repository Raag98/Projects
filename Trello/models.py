from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=50)
    createdOn = models.DateTimeField(
        default=timezone.now
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    createdOn = models.DateTimeField(
        default=timezone.now
    )
    dueDate = models.DateTimeField()
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name