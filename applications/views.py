from django.shortcuts import render, redirect, get_object_or_404
from .models import students
from accounts.models import Moderator_base
from .forms import StudentApplicationForm

def create_application_view(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applications:application_list')
    else:
        form = StudentApplicationForm()
    
    context = {
        'form': form
    }
    return render(request, 'applications/create_applications.html', context)

def application_list(request):
    applications = students.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'applications/application_review.html', context)

def reject_application(request, application_id):
    application = students.objects.get(id=application_id)
    application.reject_application()
    # Дополнительные действия, если необходимо
    return redirect('applications:application_list')

def accept_application(request, application_id):
    application = students.objects.get(id=application_id)
    application.accept_application()
    # Дополнительные действия, если необходимо
    return redirect('applications:application_list')