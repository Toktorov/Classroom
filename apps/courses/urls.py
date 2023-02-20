from django.urls import path 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.courses import views

router = DefaultRouter()
router.register(prefix='courses', viewset=views.CourseAPIViewSet)

urlpatterns = router.urls