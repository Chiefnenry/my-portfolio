from django.db import models

# Create your models here.

class MyInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField ()
    subject = models.CharField(max_length=50)
    messages = models.CharField(max_length=5000)
    