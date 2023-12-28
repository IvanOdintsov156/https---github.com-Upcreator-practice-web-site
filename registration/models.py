import datetime
from accounts.models import Regions
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ADMIN(models.Model):
    user_name = models.CharField("Имя",max_length=50,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),)
    first_name = models.CharField("Фамилия",max_length=150)
    last_name = models.CharField("Отчество",max_length=150)
    password = models.CharField("Пароль",max_length=500)
    e_mail = models.CharField("Почта",max_length=150)
    telephone_number = models.CharField("Почта",max_length=30)
    user_post = models.CharField("Должность", max_length=150)
    structural_subdivision = models.CharField("Структурное подразделение", max_length=150)
    region = models.CharField("Регион присутствия", max_length=150,default=" ")

    def __str__(self):
        return self.user_name

    '''def save(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def delete(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def set_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def check_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )'''

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"