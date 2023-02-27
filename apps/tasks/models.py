from django.db import models
from django.contrib.auth import get_user_model

from apps.courses.models import Course

User = get_user_model()

# Create your models here.
class Theme(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_themes"
    )
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
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="users_tasks",
        verbose_name="Пользователь",
        null=True
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

class SendTask(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="task_user",
        verbose_name="Пользователь"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="users_send_tasks"
    )
    url = models.URLField(
        verbose_name="Ссылка"
    )
    file = models.FileField(
        upload_to="send_tasks/",
        verbose_name="Файл"
    )
    point = models.PositiveIntegerField(
        default=0,
        verbose_name="Оценка задания"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} {self.task}"
    
    class Meta:
        verbose_name = "Отправить задание"
        verbose_name_plural = "Отправить задание"