from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    # this means if a user is deleted delete the profile, but not vise versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics' )


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        # runs the parent function that would have otherwise run
        super().save()

        # Resize large images
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        