from django.shortcuts import render, redirect
from band_app.models import *
from band_app.forms import BlogForm

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

def new_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('blog')
    
    else: 
        form = BlogForm()

    return render(request, 'band/new_post.html',{'form': form})

def blog_detail(request, blog_id):
    details = Blog.objects.get(id = blog_id )
    return render(request, 'band/blog_detail.html', {'details': details})

def delete(request,blog_id):
    blog_delete = Blog.objects.get(id = blog_id)
    blog_delete.delete()
    return redirect('blog')