from django.shortcuts import render
from band_app.models import *

# Create your views here.
def home(request):
    concerts = Concert.objects.all()
    return render(request, 'band/index.html', {'concerts': concerts})

def about(request):
    gallerys = Concert.objects.all()
    return render(request, 'band/about.html',{'gallerys': gallerys} )

def tours(request):
    gallerys = Concert.objects.all()
    return render(request, 'band/tours.html',{'gallerys': gallerys} )

def blog(request):
    gallerys = Concert.objects.all()
    return render(request, 'band/blog.html',{'gallerys': gallerys} )
