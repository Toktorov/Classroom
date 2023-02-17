from django.db import models

from apps.users.models import User

# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        related_name="users_courses",
        null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название курса"
    )
    section = models.CharField(
        max_length=255,
        verbose_name="Раздел",
        blank=True, null=True
    )
    subject = models.CharField(
        max_length=255,
        verbose_name="Предмет",
        blank=True, null=True
    )
    audience = models.CharField(
        max_length=255,
        verbose_name="Аудитория",
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.user} {self.name}"
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"