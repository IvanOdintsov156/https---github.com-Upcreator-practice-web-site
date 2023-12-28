from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from .models import ADMIN
from django.contrib.auth.models import User
from django_email_verification import send_email


def index(request):
    return HttpResponse("Hello METANIT.COM")


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #user = form.save()
            # сохранение номера
            raw_password = make_password(form.cleaned_data.get('password1'))
            ADMIN.objects.create(user_name=form.cleaned_data.get('user_name'),
                                  first_name=form.cleaned_data.get('first_name'),
                                    last_name=form.cleaned_data.get('last_name'),
                                      password=raw_password, e_mail=form.cleaned_data.get('e_mail'),
                                        telephone_number=form.cleaned_data.get('telephone_number'),
                                          user_post=form.cleaned_data.get('user_post'), structural_subdivision=form.cleaned_data.get('structural_subdivision'),
                                            region=form.cleaned_data.get('region'))
            '''user = authenticate(username=form.cleaned_data.get('user_name'), password=form.cleaned_data.get('password1'))
            login(request, user)
            user.is_active = False
            send_email(user)'''
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})