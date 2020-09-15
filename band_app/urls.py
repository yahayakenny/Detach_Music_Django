from django.urls import path
from band_app.views import *
from band_app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('tours/', views.tours, name = 'tours'),
    path('blog/', views.blog, name = 'blog'),

]