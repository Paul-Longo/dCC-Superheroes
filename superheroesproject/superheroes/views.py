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
        superhero_name = request.POST.get('superhero_name')
        alter_ego = request.POST.get('alter_ego')
        primary_super_power = request.POST.get('primary_super_power')
        secondary_super_power = request.POST.get('secondary_super_power')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego=alter_ego, primary_super_power=primary_super_power,
                                  secondary_super_power=secondary_super_power, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def update(request, superhero_id):
    if request.method == 'POST':
        update_hero = Superhero.objects.get(pk=superhero_id)
        update_hero.superhero_name = request.POST.get('superhero_name')
        update_hero.alter_ego = request.POST.get('alter_ego')
        update_hero.primary_super_power = request.POST.get(
            'primary_super_power')
        update_hero.secondary_super_power = request.POST.get(
            'secondary_super_power')
        update_hero.catchphrase = request.POST.get('catchphrase')
        update_hero.save()
        return detail(request, superhero_id)
    else:
        update_hero = Superhero.objects.get(pk=superhero_id)
        context = {
            'update_hero': update_hero
        }
        return render(request, 'superheroes/update.html', context)


def delete(request, superhero_id):
    Superhero.objects.filter(pk=superhero_id).delete()
    return HttpResponseRedirect(reverse('superheroes:index'))
