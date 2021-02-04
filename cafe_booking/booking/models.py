from django.db import models

class Booking(models.Model):
    First_Name = models.CharField(max_length=5, default="")
    Last_Name = models.CharField(max_length=50,default="")
    DateTime = models.DateTimeField()
    HeadCount = models.PositiveIntegerField(default=1)
