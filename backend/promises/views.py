from django.shortcuts import render
from .forms import PromiseForm
from promises.models import Promise

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'promises/index.html')

def how(request):
    return render(request, 'promises/how-it-works.html')

def create(request):
    return render(request, 'promises/create-deal.html')

def final(request):
    if request.method == 'POST':
        details = PromiseForm(request.POST)
        print(request.POST['name'])
        print(request.POST['email'])

        if details.is_valid(): 
            promise = details.save(commit = False)
            promise.save() 
            return render(request, 'promises/final-deal.html', {'promise':promise})
        else:
            return render(request, "promises/create-deal.html", {'form':details}) 
    else:
        form = PromiseForm(None)  
        return render(request, 'promises/final-deal.html', {'form':form})

def report(request, short_link):
    try:
        promise = Promise.objects.get(short_link=short_link)
    except Promise.DoesNotExist:
        raise Http404("Promise does not exist")
    return render(request, 'promises/reporter-main.html', {'promise': promise})