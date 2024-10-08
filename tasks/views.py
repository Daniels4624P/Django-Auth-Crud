from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import CreateTaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) #Create the model user
                user.save() #save the user in the database
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                return render(request, "signup.html", {'form': UserCreationForm(), 'error': 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Password do not match'})

@login_required 
def tasks(request):
    tareas = Task.objects.filter(user=request.user, date_completed__isnull=True).order_by()
    return render(request, 'tasks.html', {'tasks': tareas})

@login_required
def delete_session(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm(), 'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('tasks')

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': CreateTaskForm()})
    else:
        try:
            form = CreateTaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {'form': CreateTaskForm(), 'error': 'Please provide valide data'})

@login_required
def get_task(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk= task_id, user=request.user)
        form = CreateTaskForm(instance=task)
        return render(request, 'get_task.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = CreateTaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except:
            return render(request, 'get_task.html', {'task': task, 'form': form, 'error': 'Error updating task'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
def tasks_completed(request):
    task = Task.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'tasks.html', {'tasks': task})