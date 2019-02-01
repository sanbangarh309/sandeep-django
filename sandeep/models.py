from django.db import models

# Create your models here.
class Users(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
