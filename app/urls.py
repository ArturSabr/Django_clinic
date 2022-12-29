from .views import *
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',home,name='home'),
    path('doctor/', doctors,name='doctors'),
    path('about_us/', about,name='aboutus'),
    path('price/', price,name='price'),
    path('register/', register,name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(),name='logout'),
    path('doctor/<int:id>', more, name='detail'),
    path('entry/', add ,name='entry'),
]