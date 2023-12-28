from django.db import models
from django.contrib.auth.models import User


class Regions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион присутствия"
        verbose_name_plural = "Регионы присутствия"


class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Moderator_base(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("Имя", max_length=255)
    second_name = models.CharField("Фамилия", max_length=255)
    middle_name = models.CharField("Отчество", max_length=255)
    subdivision = models.CharField("Название подразделения", max_length=255, default=" ")
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    phone_number = models.CharField("Номер телефона", max_length=17)
    email = models.EmailField("Почта")
    post = models.CharField("Должность", max_length=255, default=" ")
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Модератор"
        verbose_name_plural = "Модераторы"