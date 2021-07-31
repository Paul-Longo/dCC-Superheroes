from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def create(request):
    if request.method == 'POST':
        superhero_name = request.Post.get('superhero_name')
        alter_ego = request.Post.get('alter_ego')
        primary_super_power = request.Post.get('primary_super_power')
        secondary_super_power = request.Post.get('secondary_super_power')
        catchphrase = request.Post.get('catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego=alter_ego, primary_super_power=primary_super_power, secondary_super_power=secondary_super_power, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')