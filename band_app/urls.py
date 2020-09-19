from django.urls import path
from band_app.views import *
from band_app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('tours/', views.tours, name = 'tours'),
    path('blog/', views.blog, name = 'blog'),
    path('blog/<int:blog_id>', views.blog_detail, name = 'blog_detail'),
    path('delete/<int:blog_id>', views.delete, name='blog_delete'),
    path('new_post/', views.new_post, name = 'new_post'),

    

]