from django.db import models

# Create your models here.


class Course(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='courses', on_delete=models.CASCADE)
    highlighted = models.TextField()

    course_id = models.CharField(max_length=10, primary_key=True)
    course_title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    credit = models.IntegerField()
    semester_offered = models.CharField(max_length=50)

    class Meta:
        ordering = ['course_id']

    def __str__(self):
        return self.course_title
