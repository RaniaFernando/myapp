from django.urls import path
from .views import CourseViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CourseListCreateView, CourseDetailView,
    CourseInstanceCreateView, CourseInstanceListView, CourseInstanceDetailView
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/', CourseInstanceCreateView.as_view(), name='instance-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListView.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetailView.as_view(), name='instance-detail'),
        path('admin/', admin.site.urls),
    path('api/', include('course_management.urls')),  # Includes app-level routes
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('course_management.urls')),  # Includes app-level routes
# ]

