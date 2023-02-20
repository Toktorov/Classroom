from rest_framework import serializers

from apps.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'user', 'name',
                  'section', 'subject', 'audience')