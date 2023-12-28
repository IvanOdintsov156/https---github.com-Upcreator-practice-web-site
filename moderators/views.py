from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PracticeCreateForm,PracticeEditForm
from .models import Practice
from django.core.paginator import Paginator
from accounts.models import Moderator_base

def moderator_dashboard(request):
    moderators = Moderator_base.objects.all()
    return render(request, 'moderators/moderator_dashboard.html', {'moderators': moderators})

def create_practice(request):
    if request.method == 'POST':
        form = PracticeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moderators:practice_list')
    else:
        form = PracticeCreateForm()
    return render(request, 'moderators/practice_create_form.html', {'form': form})

def practice_list(request):
    practices = Practice.objects.all()
    paginator = Paginator(practices, 10)  # Разделение на страницы, по 10 практик на страницу
    page = request.GET.get('page')  # Получение номера текущей страницы из GET-параметра

    practices = paginator.get_page(page)

    return render(request, 'moderators/practice_list.html', {'practices': practices})

def edit_practice(request, practice_id):
    practice = get_object_or_404(Practice, id=practice_id)

    if request.method == 'POST':
        form = PracticeEditForm(request.POST, instance=practice)
        if form.is_valid():
            form.save()
            return redirect('moderators:practice_list')
    else:
        form = PracticeEditForm(instance=practice)

    return render(request, 'moderators/edit_practice.html', {'form': form, 'practice': practice})

def delete_practice(request, practice_id):
    practice = get_object_or_404(Practice, id=practice_id)

    if request.method == 'POST':
        practice.delete()
        return redirect('moderators:practice_list')

    return render(request, 'moderators/delete_practice.html', {'practice': practice})