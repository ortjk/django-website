import os

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content")
    date_posted = models.DateTimeField("Date Posted", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("Image", default="post_images/default.png", upload_to="post_images")

    def __str__(self):
        return self.title

# media files are not automatically deleted by django when their parent Post is deleted.
# this is a function which uses the receiver to run itself when a Post is deleted,
# and then deletes the corresponding media using os.
@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
