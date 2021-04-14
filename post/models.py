from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    icon_url  = models.CharField(blank=True, default="", max_length=1000)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:post_list_by_slug', args=[self.slug])


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'DRAFT'),
                      ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, default=0)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    jourj = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    likes = models.ManyToManyField(get_user_model(), related_name="posts_liked", blank=True)
    shares = models.ManyToManyField(get_user_model(), related_name="posts_shared", blank=True)

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.slug])


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    likes = models.ManyToManyField(get_user_model(), related_name="comments_liked", blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Commented by {self.name}"





