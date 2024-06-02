from django.shortcuts import render
from task.models import taskModel


def home(request):
    tasks = taskModel.objects.all()
    return render(request,'home.html',{'tasks':tasks})


