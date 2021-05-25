from django.db import models

from products.models import Product
from profiles.models import UserProfile


class ProductReview(models.Model):
    """
    Model will allow users to perform
    CRUD operations on products of choice
    """

    RATE_CHOICES = [
        (1, '1 - Bad'),
        (2, '2 - Average'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Great'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=3)
    body = models.TextField(max_length=3000, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user
