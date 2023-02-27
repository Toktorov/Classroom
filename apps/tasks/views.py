from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import mixins

from apps.tasks.models import Theme, Task
from apps.tasks.serializers import ThemeSerializer, TaskSerializer

# Create your views here.
class ThemeAPIViewSet(GenericViewSet,
                      mixins.ListModelMixin, 
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, 
                      mixins.DestroyModelMixin):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (IsAuthenticated, )

class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin, 
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)