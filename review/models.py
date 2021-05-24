from django.db import models

from products.models import Product
from profiles.models import UserProfile



class ProductReview(models.Model):
    """
    Model will allow users to perform
    CRUD operations on products of choice
    """

    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATE_CHOICES)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
