from django.db import models
from django.contrib.auth.models import User
from book_app.models import Book

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items= models.ManyToManyField(Book)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items_cart')
    book = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items_book')
    quantity = models.PositiveIntegerField(default=1)


