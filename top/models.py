from django.db import models
from django.utils import timezone

class UpdateInfo(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField()
    body = models.TextField()
    is_public = models.BooleanField('Public Article?', default=True)
    created_at = models.DateTimeField('Created at', default=timezone.now)
    updated_at = models.DateTimeField('Updated at', default=timezone.now)

    def __str__(self):
        return self.title