from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method== 'GET':
        print('Enviando formulario')
    else:
        print('Obteniendo datos')



    return render(request, 'signup.html',{
    'form':UserCreationForm
    })