from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    username = models.CharField(max_length=255)