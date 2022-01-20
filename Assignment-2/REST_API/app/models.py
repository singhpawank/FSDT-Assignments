from django.db import models
import uuid

# Create your models here.

# User Model
class User(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)  # Autogenerate
    name = models.CharField(max_length=50)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)

# Event Model
class Event(models.Model):
    id = models.AutoField(primary_key=True) # Autogenerate
    user_id = models.ForeignKey('User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    OCCURANCE_CHOICES = (
        ('O', 'ONETIME'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY'),
    )

    occurance = models.CharField(max_length=1, choices=OCCURANCE_CHOICES)
    startDate = models.DateField()
    endDate = models.DateField()
