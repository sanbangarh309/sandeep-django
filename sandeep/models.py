from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    image = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    when = models.DateTimeField("date created", auto_now_add=True)


class Projects(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=60)
    image = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    when = models.DateTimeField("date created", auto_now_add=True)
