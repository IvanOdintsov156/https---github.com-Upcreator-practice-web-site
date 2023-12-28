from django.urls import path
from .views import (
    moderator_dashboard,
    create_practice,
    practice_list,
    moderator_dashboard,
    edit_practice,
    delete_practice
)

app_name = 'moderators'

urlpatterns = [
    path('moderator_dashboard/', moderator_dashboard, name='moderator_dashboard'),
    path('create_practice/', create_practice, name='create_practice'),
    path('practice_list/', practice_list, name='practice_list'),
    path('practice/<int:practice_id>/edit/', edit_practice, name='edit_practice'),
    path('practice/<int:practice_id>/delete/', delete_practice, name='delete_practice'),
]
