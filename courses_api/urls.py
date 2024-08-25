from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course_management.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Includes the API routes from the course_management app
]
