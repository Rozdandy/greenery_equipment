from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    overview = models.TextField()
    article = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    article = models.TextField()

    def __str__(self):
        return self.name
