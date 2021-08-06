from django.db import models

# Create your models here.


class Superhero(models.Model):
    superhero_name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=50)
    primary_super_power = models.CharField(max_length=100)
    secondary_super_power = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=150)

    def __str__(self):
        return self.superhero_name
