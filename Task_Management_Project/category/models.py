from django.db import models

# Create your models here.
from task.models import TaskModel

class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.categoryName

