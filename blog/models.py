from django.db import models
from django.utils import timezone  # 追加


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('タイトル', max_length=100)
    thumbnail = models.ImageField('サムネイル')
    Tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='タグ')
    text = models.TextField('本文', blank=True)
    is_public = models.BooleanField('公開可能か?', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title