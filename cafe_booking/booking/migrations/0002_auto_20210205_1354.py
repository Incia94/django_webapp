# Generated by Django 3.1.6 on 2021-02-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='snack',
            field=models.CharField(blank=True, choices=[('1', 'French Fries'), ('2', 'Aloo Tikki'), ('3', 'Dahi Chaat'), ('4', 'Honey Chilli Potato'), ('5', 'Cheese Fries')], max_length=50, null=True),
        ),
    ]