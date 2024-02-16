from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html', {'dests':dests})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')





