from django.contrib import admin
from django.urls import path, include
from registration.views import registration, index
from django_email_verification import urls as email_urls

urlpatterns = [
    path('', index),
    path('user/', registration),
    path('email/', include(email_urls)),
]