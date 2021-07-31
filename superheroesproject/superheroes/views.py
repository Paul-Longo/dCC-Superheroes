from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero
# Create your views here.

def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, superhero_id):
    single_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'single_superhero': single_superhero
    } 
    return render(request, 'superheroes/detail.html', context)