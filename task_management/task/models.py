from django.db import models
from category.models import categoryModel

# Create your models here.


class taskModel(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    taskCategory = models.ManyToManyField(categoryModel)
    taskAssignDate = models.DateField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle
    