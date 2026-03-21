from django.db import models
from django.contrib.auth.models import User

from Products.models import Product

# Create your models here.


class Cart(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Кошик (active-{self.active})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Додати до кошика товар '{self.product}' {self.quantity} шт."
