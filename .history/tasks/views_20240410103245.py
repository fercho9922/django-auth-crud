from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User
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


def tasks(request):
    return render(request, 'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')
