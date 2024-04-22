from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
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
        if request.POST['password1']==request.POST['password']:
            #Registrar usuario
            try:
                user= User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('Username already exists')
        
        return HttpResponse('PASSWORD do not match')
        print(request.POST)
        print('Obteniendo datos')



   