from django.db import models

# Create your models here.
class Concert(models.Model):
    image = models.ImageField(blank = True, null = True)
    
class Event(models.Model):
    image1 = models.ImageField(blank = True, null = True)
    artiste1 = models.CharField(max_length=50, blank = True, null = True)
    date1 = models.CharField(max_length=50, blank = True, null = True)

    image2 = models.ImageField(blank = True, null = True)
    artiste2 = models.CharField(max_length=50, blank = True, null = True)
    date2 = models.CharField(max_length=50, blank = True, null = True)

    image3 = models.ImageField(blank = True, null = True)
    artiste3 = models.CharField(max_length=50, blank = True, null = True)
    date3 = models.CharField(max_length=50, blank = True, null = True)

class Team(models.Model):
    image = models.ImageField(blank = True, null = True)
    name = models.CharField(max_length=50, blank = True, null = True)
    role = models.CharField(max_length=50, blank = True, null = True)


class Tour(models.Model):
    image = models.ImageField(blank = True, null = True)
    name = models.CharField(max_length=50, blank = True, null = True)
    date = models.CharField(max_length=50, blank = True, null = True)
    venue = models.CharField(max_length=50, blank = True, null = True)
    description = models.CharField(max_length=200, blank = True, null = True)
    slug = models.SlugField()
    price = models.FloatField(default=1)


class Blog(models.Model):
    image = models.ImageField(blank = True, null = True)
    title =  models.CharField(max_length=50, blank = True, null = True)
    author = models.CharField(max_length=50, blank = True, null = True)
    description = models.CharField(max_length=200, blank = True, null = True)
   
   