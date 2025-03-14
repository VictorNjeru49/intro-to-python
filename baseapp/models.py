from django.db import models

# Create your models here.
class Features(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)