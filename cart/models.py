from django.db import models
from django.contrib.auth.models import User
from api_basic.models import Course
from django.dispatch import receiver


from django.db.models.signals import pre_save, post_save
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oredered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Course, on_delete=models.CASCADE)
    # total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
