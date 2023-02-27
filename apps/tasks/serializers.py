from rest_framework import serializers

from apps.tasks.models import Theme, Task


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'course', 'title')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = ('id', 'course', 'title', 'user',
                  'description', 'points', 'deadline',
                  'theme', 'url_task', 'file_task')