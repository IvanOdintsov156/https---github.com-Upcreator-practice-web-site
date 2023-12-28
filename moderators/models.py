from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from accounts.models import Regions, Speciality, Moderator_base

class TrainingDirections(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Направление практики'
        verbose_name_plural = 'Направления практики'
 
class Practice(models.Model):
    direction = models.ForeignKey(TrainingDirections, verbose_name='Направление практики', on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, verbose_name='Регион', on_delete=models.CASCADE)
    practice_director_full_name = models.CharField(max_length=255, verbose_name='ФИО руководителя практики')
    name_of_PSK_or_structure = models.CharField(max_length=255, verbose_name='Название ПСК или структуры')
    need_amount_of_practicants = models.IntegerField(verbose_name='Требуемое количество практикантов')
    practice_description = models.TextField(verbose_name='Описание практики')
    required_skills = models.TextField(verbose_name='Требуемые навыки/квалификации')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    def __str__(self):
        return self.name_of_PSK_or_structure

    class Meta:
        verbose_name = _('Создание практики')
        verbose_name_plural = _('Создание практики')