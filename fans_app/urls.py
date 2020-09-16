from django.urls import path
from fans_app.views import *
from fans_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'fans/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'fans/logout.html'), name='logout'), 

]