from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'accounts'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('register/', views.sign_up, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('log_in/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
]