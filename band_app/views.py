from django.shortcuts import render
from band_app.models import *

# Create your views here.
def home(request):
    events = Event.objects.all()
    return render(request, 'band/index.html', {'events': events})

def about(request):
    gallerys = Concert.objects.all()
    teams = Team.objects.all()
    return render(request, 'band/about.html',{'gallerys': gallerys, 'teams':teams})

def tours(request):
    gallerys = Concert.objects.all()
    tours = Tour.objects.all()
    return render(request, 'band/tours.html',{'gallerys': gallerys, 'tours': tours} )

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'band/blog.html',{'blogs': blogs} )
