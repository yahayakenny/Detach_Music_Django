from django.db import models
from django.shortcuts import reverse

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
  
   

class Blog(models.Model):
    
    title =  models.CharField(max_length=50, blank = True, null = True)
    author = models.CharField(max_length=50, blank = True, null = True)
    caption = models.CharField(max_length=100, blank = True, null = True)
    description = models.CharField(max_length=1000, blank = True, null = True)
    
   