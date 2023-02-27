from django.contrib import admin

from apps.tasks.models import Theme, Task, SendTask

# Register your models here.
admin.site.register(Theme)
admin.site.register(Task)
admin.site.register(SendTask)