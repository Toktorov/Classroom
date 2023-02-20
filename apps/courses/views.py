from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins

from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer

# Create your views here.
class CourseAPIViewSet(GenericViewSet, 
                    mixins.ListModelMixin, 
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), )
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)