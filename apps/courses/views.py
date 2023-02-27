from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins

from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer, CourseDetailSerializer
from apps.courses.permissions import CoursesPermissions

# Create your views here.
class CourseAPIViewSet(GenericViewSet, 
                    mixins.ListModelMixin, 
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), CoursesPermissions())
        return (IsAuthenticated(), )
    
    def filter_queryset(self, queryset):
        return Course.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)