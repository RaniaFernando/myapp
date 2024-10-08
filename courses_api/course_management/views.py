from rest_framework import viewsets, generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# ViewSet for Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# API Views for Course
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# API Views for CourseInstance
class CourseInstanceCreateView(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceListView(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
