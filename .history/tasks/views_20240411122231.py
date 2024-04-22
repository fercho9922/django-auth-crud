from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import TaskForm
from .forms import task
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            #Registrar usuario
            try:
                user= User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')

            except IntegrityError:
                return render(request, 'signup.html', {
                'form':UserCreationForm,
                "error": 'USername already exist'
                })  

        return render(request, 'signup.html', {
                'form':UserCreationForm,
                "error": 'Password do not match'
                })  
        print(request.POST)
        print('Obteniendo datos')


def create_task(request):
    
    if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form':TaskForm
    })
    else:
        try:
            form=TaskForm(request.POST)
            new_task=form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render (request, 'create_task.html',{
            'form': TaskForm,
            'error': 'please provide valida data'
            })
            

def task_detail(request, task_id):
    tarea=get_object_or_404(task,pk=task_id)
    form=TaskForm(instance=task)
    return render(request, 'task_detail.html',{'task':tarea, 'form':form})
    

        

def tasks(request):
    tasks=task.objects.all()
    return render(request, 'tasks.html',{'tasks': tasks})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
   if request.method == 'GET':
    return render(request, 'signin.html',{
    'form': AuthenticationForm
    
    })
   else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            print(request.POST)
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')       
    
        



