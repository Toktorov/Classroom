# Generated by Django 4.1.7 on 2023-02-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=8, unique=True, verbose_name='Код курса'),
        ),
    ]
