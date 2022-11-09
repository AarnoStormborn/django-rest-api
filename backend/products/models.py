from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Product'