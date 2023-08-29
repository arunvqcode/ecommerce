from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductDetails(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    items = models.ManyToManyField(ProductDetails, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='CartItem')
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)