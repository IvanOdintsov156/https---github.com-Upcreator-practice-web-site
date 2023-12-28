from django.urls import path
from .views import create_application_view, application_list, reject_application, accept_application
app_name = 'applications'
urlpatterns = [
    path('create_application/', create_application_view, name='create_application_view'),
    path('application_list/', application_list, name='application_list'),
    path('reject_application/<int:application_id>/', reject_application, name='reject_application'),
    path('accept_application/<int:application_id>/', accept_application, name='accept_application'),
]
