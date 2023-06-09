from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def total_price(self):
        if self.discount_price:
            return self.price - self.discount_price
        else:
            return self.price
