from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.tasks import views

router = DefaultRouter()
router.register(prefix='theme', viewset=views.ThemeAPIViewSet)
router.register(prefix='task', viewset=views.TaskAPIViewSet)

urlpatterns = router.urls