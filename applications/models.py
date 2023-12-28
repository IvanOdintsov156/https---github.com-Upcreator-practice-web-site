from django.db import models
from moderators.models import TrainingDirections, Regions

class students(models.Model):
    STATUS_CHOICES = (
        ("Рассмотрение", "Рассмотрение"),
        ("Отклонено", "Отклонено"),
        ("Принято", "Принято"),
    )
    practice = models.ForeignKey(TrainingDirections, on_delete=models.CASCADE, verbose_name="Направление практики")
    full_name = models.CharField("ФИО", max_length=250)
    email = models.EmailField(max_length=254, verbose_name="Почта")
    phone_number = models.CharField("Номер телефона", max_length=18)
    status = models.CharField("Статус", max_length=255, choices=STATUS_CHOICES)
  
    def reject_application(self):
        self.status = "Отклонено"
        self.save()
  
    def accept_application(self):
        self.status = "Принято"
        self.save()