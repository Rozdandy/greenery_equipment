from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    article = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
