from django.db import models


class Menu(models.Model):
    snack_choices = (
        ('1', u'French Fries'),
        ('2', u'Aloo Tikki'),
        ('3', u'Dahi Chaat'),
        ('4', u'Honey Chilli Potato'),
        ('5', u'Cheese Fries'),
    )

    dessert_choices = (
        ('1', u'Banoffe Pie'),
        ('2', u'Tiramisu'),
        ('3', u'Brownie'),
        ('4', u'Cheesecake'),
    )

    snack = models.CharField(max_length=50, choices=snack_choices, null=True, blank=True)
    dessert = models.CharField(max_length=50, choices=dessert_choices, null=True, blank=True)


class Booking(models.Model):
    First_Name = models.CharField(max_length=5, default="")
    Last_Name = models.CharField(max_length=50, default="")
    DateTime = models.DateTimeField()
    HeadCount = models.PositiveIntegerField(default=1)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
