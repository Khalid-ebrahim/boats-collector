from django.db import models

# Create your models here.

class Boat(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    description = models.TextField(max_length=250)
    production = models.CharField(max_length=100)
    # image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')