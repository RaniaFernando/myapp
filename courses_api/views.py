from rest_framework import generics, viewsets
from .models import Course, CourseInstance # type: ignore
from .serializers import CourseSerializer, CourseInstanceSerializer # type: ignore
from .views import CourseViewSet
from courses_api.course_management.views import CourseViewSet


# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of courses or create a new course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a course by ID.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# CourseInstance Views
class CourseInstanceCreateView(generics.CreateAPIView):
    """
    API view to create a new course instance.
    """
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceListView(generics.ListAPIView):
    """
    API view to retrieve a list of course instances for a specific year and semester.
    """
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

class CourseInstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a course instance by ID.
    """
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

# Optional: ViewSet if you're using routers
class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the Course model.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
