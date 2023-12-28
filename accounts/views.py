from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, ModeratorForm
from .models import Moderator_base
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import Group, User


def index(request):
    return render(request, 'accounts/profile.html')


def sign_up(request):
    if request.method == 'GET':
        reg_form = RegisterForm()
        staff_form = ModeratorForm()
        return render(request, 'accounts/register.html', {'reg_form': reg_form, 'staff_form': staff_form})

    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        staff_form = ModeratorForm(request.POST)
        if reg_form.is_valid() and staff_form.is_valid():
            user = reg_form.save(commit=False)
            user.username = user.email
            user.save()
            messages.success(request, 'You have singed up successfully.')
            a = Moderator_base(user=user,
                                      first_name=staff_form.cleaned_data['first_name'],
                                      second_name=staff_form.cleaned_data['second_name'],
                                      middle_name=staff_form.cleaned_data['middle_name'],
                                      subdivision=staff_form.cleaned_data['subdivision'],
                                      position=staff_form.cleaned_data['position'],
                                      phone_number=staff_form.cleaned_data['phone_number'],
                                      email=user.email,
                                      post = staff_form.cleaned_data['post'],
                                      )
            a.save()
            return redirect('accounts:profile')
        else:
            return render(request, 'accounts/register.html', {'reg_form': reg_form, 'staff_form': staff_form})


def log_out(request):
    logout(request)
    return redirect('accounts:log_in')


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('accounts:index')
            else:
                return HttpResponseRedirect(reverse('accounts:log_in'))
        else:
            return HttpResponseRedirect(reverse('accounts:log_in'))


def profile(request):

    return render(request, 'accounts/profile.html')