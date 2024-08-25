from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    year_of_delivery = models.IntegerField()
    semester_of_delivery = models.IntegerField(choices=[(1, 'First'), (2, 'Second')])

    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField(choices=[(1, 'First'), (2, 'Second')])

    def __str__(self):
        return f"{self.course.title} - {self.year}/{self.semester}"
