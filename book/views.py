from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
# Create your views here.

def BookView(request):
    model = Book
    template_name = "viewbook.html"

    return render(request, 'viewbook.html', {})

def Test(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

# def AddBook(request):
