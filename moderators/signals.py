'''# moderators/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Application, PracticeRequest
from django.contrib.auth.models import User

# Helper function to send email notifications for a practice request
def send_email_notification(user, practice_request):
    send_mail(
        'Новая практика в вашей специальности: {0}'.format(practice_request.title),
        'Здравствуйте, {0}!\n\nМы рады сообщить вам о новой практике "{1}" в специальности "{2}". Подробности вы можете найти на нашем сайте.'.format(user.first_name, practice_request.title, practice_request.training_speciality),
        'from@example.com',
        [user.email],
        fail_silently=False,
    )

# Signal to send notifications upon Application creation
@receiver(post_save, sender=Application)
def application_created(sender, instance, created, **kwargs):
    if created and instance.specialty_matches():  # Assuming specialty_matches is a method on Application
        # Send notification to the admin
        send_mail(
            'Новая заявка на практику',
            'Текст сообщения администратору.',
            'from@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )
        
        # Send notification to the user
        send_mail(
            'Ваша заявка на практику принята',
            'Текст сообщения пользователю.',
            'from@example.com',
            [instance.user.email],  # Assuming Application has a user relationship
            fail_silently=False,
        )

# Signal to send notifications upon PracticeRequest creation
@receiver(post_save, sender=PracticeRequest)
def practice_request_created(sender, instance, created, **kwargs):
    if created:
        # Get users with a matching training specialty
        matching_users = User.objects.filter(profile__training_speciality=instance.training_speciality)
        
        # Send an email notification to each matching user
        for user in matching_users:
            send_email_notification(user, instance)'''