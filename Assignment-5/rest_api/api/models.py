from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50,  null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)

class item(models.Model):
    user_uid = models.ForeignKey('user', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)

class booking(models.Model):
    user_uid = models.ForeignKey('user', on_delete=models.CASCADE, null=False)
    item_id = models.ForeignKey('item', on_delete=models.CASCADE, null=False)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)

    class Meta:
        unique_together = ('user_uid', 'item_id')