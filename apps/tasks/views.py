from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from apps.tasks.models import Theme, Task, SendTask
from apps.tasks.serializers import ThemeSerializer, TaskSerializer, TaskDetailSerializer, SendTaskSerializer
from apps.tasks.permissions import TaskPermissions, SendTaskPermissions

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
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return TaskDetailSerializer
        return TaskSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), TaskPermissions())
        return (IsAuthenticated(), )

    def filter_queryset(self, queryset):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class SendTaskAPIViewSet(GenericViewSet,
                         mixins.ListModelMixin, 
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin, 
                         mixins.DestroyModelMixin):
    queryset = SendTask.objects.all()
    serializer_class = SendTaskSerializer
    permission_classes = (IsAuthenticated, SendTaskPermissions)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)