from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    price = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    ratings_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
