from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'promises/index.html')

def how(request):
    return render(request, 'promises/how-it-works.html')

def create(request):
    return render(request, 'promises/create-deal.html')

def final(request):
    return render(request, 'promises/final-deal.html')

def report(request):
    return render(request, 'promises/reporter-main.html')