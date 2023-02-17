from django.db import models

from apps.courses.models import Course

# Create your models here.
class Theme(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Тема"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Тема задания"
        verbose_name_plural = "Тема задании"

class Task(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_tasks"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True, null=True
    )
    points = models.PositiveIntegerField(
        verbose_name="Балл",
        blank=True, null=True
    )
    deadline = models.DateTimeField(
        blank=True, null=True
    )
    theme = models.ForeignKey(
        Theme,
        on_delete=models.SET_NULL,
        related_name="theme_tasks",
        blank=True, null=True
    )
    url_task = models.URLField(
        verbose_name="Ссылка",
        blank=True, null=True
    )
    file_task = models.FileField(
        upload_to="files_task",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задании"