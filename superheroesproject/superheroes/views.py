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

def update(request, superhero_id):
    if request.method == 'POST':
        updated_hero = Superhero.objects.get(pk=superhero_id)
        updated_hero.superhero_name = request.Post.get('superhero_name')
        updated_hero.alter_ego = request.Post.get('alter_ego')
        updated_hero.primary_super_power = request.Post.get('primary_super_power')
        updated_hero.secondary_super_power = request.Post.get('secondary_super_power')
        updated_hero.catchphrase = request.Post.get('catchphrase')
        updated_hero.save()
        return detail(request, superhero_id)
    else:
        superhero = Superhero.objects.get(pk=superhero_id)
        context = {
            'superhero': superhero
        }
        return render(request, 'superheroes/update.html', context)

def delete(request, superhero_id):
    Superhero.objects.filter(pk=superhero_id).delete()
    return HttpResponseRedirect(reverse('superheroes:index'))