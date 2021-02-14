from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
# Create your views here.

def BookView(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'viewbook.html', {
        'form': BookForm(),
    })

def Test(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

def AddBook(request):
    if request.method == 'POST':
	form = BookForm(request.POST)
	if form.is_valid():
	    form.save()
	    return redirect('/')
    return render(request, 'viewbook.html', {
	'form': BookForm(),
    })
