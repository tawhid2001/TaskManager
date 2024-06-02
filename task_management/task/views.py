from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import taskModel

# Create your views here.


def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    else:
        task_form = TaskForm()

    return render(request,'task.html',{'form':task_form})

def edit_task(request,id):
    tasks = taskModel.objects.get(pk=id)
    task_form = TaskForm(instance=tasks)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=tasks)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
        

    return render(request,'task.html',{'form':task_form})

def delete_task(request,id):
    task = taskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')