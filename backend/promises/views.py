from django.shortcuts import render, redirect
from .forms import PromiseForm
from promises.models import Promise, Document
from datetime import datetime, timezone
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DocumentForm
from django.template import RequestContext
from django.urls import reverse


def index(request):
    return render(request, 'promises/index.html')

def how(request):
    return render(request, 'promises/how-it-works.html')

def advices(request):
    return render(request, 'promises/advices.html')

def create(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['email'])
        details = PromiseForm(request.POST)

        if details.is_valid(): 
            promise = details.save(commit = False)
            promise.save()
            return redirect(final, promise.short_link) 
        else:
            return render(request, "promises/create-deal.html", {'form':details}) 
    else:
        form = PromiseForm()
        return render(request, 'promises/create-deal.html', {'form':form})

def final(request, short_link):
    try:
        promise = Promise.objects.get(short_link=short_link)
    except Promise.DoesNotExist:
        raise Http404("Promise does not exist")
    return render(request, 'promises/final-deal.html', {'promise': promise})

def report(request, short_link):
    try:
        promise = Promise.objects.get(short_link=short_link)
    except Promise.DoesNotExist:
        raise Http404("Promise does not exist")
    day_num = (datetime.now(timezone.utc) - promise.pub_date).days + 1
    return render(request, 'promises/reporter-main.html', {'promise': promise, 'day_num' : day_num})

def report_upload(request, short_link):
    try:
        promise = Promise.objects.get(short_link=short_link)
    except Promise.DoesNotExist:
        raise Http404("Promise does not exist")

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('promises.views.report_upload'))
            return render(request, 'promises/report-success.html', {'promise': promise, 'form': form})
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'promises/report-upload.html', {'promise': promise, 'form': form})
