from django.db import models

# Create your models here.
class Concert(models.Model):
    image = models.ImageField(blank = True, null = True)
    

