from django.db import models

# Create your models here.
# task/models.py
from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle
