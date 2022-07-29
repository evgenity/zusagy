from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'promises/index.html')

def how(request):
    return render(request, 'promises/how-it-works.html')