from email.policy import default
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('タイトル', max_length=100)
    thumbnail = models.ImageField(upload_to='uploads/%Y/%m/%d/', default="materials/NontalonLogo.png")
    caption = models.CharField('Caption', max_length=120, default="")
    author = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    is_public = models.BooleanField('Public Article?', default=True)
    is_picked_up = models.BooleanField('Picked up Article?', default=False)
    created_at = models.DateTimeField('Created at', default=timezone.now)
    updated_at = models.DateTimeField('Updated at', default=timezone.now)

    def __str__(self):
        return self.title