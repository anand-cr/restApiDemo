from django.db import models

# Create your models here.


class ApiView(models.Model):
    function = models.CharField(max_length=50)
    details = models.CharField(max_length=100)
