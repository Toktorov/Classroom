from rest_framework import serializers

from apps.courses.models import Course
from apps.tasks.serializers import ThemeSerializer, TaskSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'user', 'name',
                  'section', 'subject', 'audience')
        
class CourseDetailSerializer(serializers.ModelSerializer):
    course_themes = ThemeSerializer(read_only=True, many=True)
    course_tasks = TaskSerializer(read_only=True, many=True)
    
    class Meta:
        model = Course
        fields = ('id', 'user', 'name', 'section', 'subject', 
                  'audience', 'course_themes', 'course_tasks')