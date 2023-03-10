# Generated by Django 4.1.7 on 2023-02-20 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тема задания',
                'verbose_name_plural': 'Тема задании',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('points', models.PositiveIntegerField(blank=True, null=True, verbose_name='Балл')),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('url_task', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('file_task', models.FileField(blank=True, null=True, upload_to='files_task')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_tasks', to='courses.course')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theme_tasks', to='tasks.theme')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задании',
            },
        ),
    ]
