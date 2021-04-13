from django.db import models

# Create your models here.

# Subject,CatalogNumber,CourseTitle,CourseType,Dates,
# Credit,MeetingTime,Room,Instructor,TotalSeats,SeatsTaken,AvailableSeats


class Course(models.Model):
    # owner = models.ForeignKey(
    #     'auth.User', related_name='courses', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    # course_id = models.CharField(max_length=10, primary_key=True)
    # course_title = models.CharField(max_length=100)
    # instructor = models.CharField(max_length=100)
    # credit = models.IntegerField()
    # semester_offered = models.CharField(max_length=50)
    course_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=10)
    catalog_number = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_type = models.CharField(max_length=20)
    dates = models.CharField(max_length=100)
    credit = models.CharField(max_length=20)
    meeting_time = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    total_seats = models.IntegerField(null=True)
    seats_taken = models.IntegerField(null=True)
    seats_available = models.IntegerField(null=True)

    class Meta:
        ordering = ['course_id']

    def __str__(self):
        return self.course_title
