from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def helloworld(request):
    title ="Hello world"
    return render(request, 'signup.html'),{
        "mytitle":title
    }