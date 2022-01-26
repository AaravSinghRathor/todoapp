from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="default.jpeg", upload_to="profile_pics")

    def __str__(self) -> str:
        return f"{self.user.username} Profile!"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.profile_image.path)

        if image.height > 350 or image.width > 350:
            changed_size = (350, 350)
            image.thumbnail(changed_size)
            image.save(self.profile_image.path)
