from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=100)

    @property
    def sale_price(self):
        return f"{self.price*0.8:.2f}"
    
    def get_discount(self):
        
        return "1221"

    class Meta:
        verbose_name_plural = 'Product'