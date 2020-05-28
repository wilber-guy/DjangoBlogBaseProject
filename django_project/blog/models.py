from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # this makes each author sign using a forigen key there post
    # on_delete causes all users posts to delete if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.title + self.content)

    # redirect after post creation to the post redirect with the pk set to this instance pk
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})