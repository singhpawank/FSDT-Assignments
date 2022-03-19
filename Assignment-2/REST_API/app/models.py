from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    name = models.CharField(max_length=50)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)

# Event Model
class Event(models.Model):
    user_id = models.ForeignKey('User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    OCCURANCE_CHOICES = (
        ('ONETIME', 'ONETIME'),
        ('WEEKLY', 'WEEKLY'),
        ('MONTHLY', 'MONTHLY'),
        ('YEARLY', 'YEARLY'),
    )

    occurance = models.CharField(max_length=10, choices=OCCURANCE_CHOICES)
    startDate = models.DateField()
    endDate = models.DateField()
