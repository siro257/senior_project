from django.db import models

from api_basic.models import Course

# Create your models here.


class OrderItem(models.Model):
    course = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.subject


class Order(models.Model):
