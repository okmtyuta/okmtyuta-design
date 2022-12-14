from django.db import models
from django.utils import timezone  # 追加


class IllustTag(models.Model):
    name = models.CharField('タグ名', max_length=100)

    def __str__(self):
        if hasattr(self, 'illust_count'):
            return f'{self.name}({self.illust_count})'
        else:
            return self.name


class Illust(models.Model):
    title = models.CharField('タイトル', max_length=100)
    illust = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    caption = models.CharField('Caption', max_length=120, default="")
    author = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    illust_tags = models.ManyToManyField(IllustTag, verbose_name='タグ', blank=True)
    is_public = models.BooleanField('Public Illust?', default=True)
    is_picked_up = models.BooleanField('Picked up Article?', default=False)
    created_at = models.DateTimeField('Created at', default=timezone.now)
    updated_at = models.DateTimeField('Updated at', default=timezone.now)

    def __str__(self):
        return self.title


class IllustComment(models.Model):
    """記事に紐づくコメント"""
    name = models.CharField('名前', max_length=255, default='Anonymous')
    text = models.TextField('本文')
    target = models.ForeignKey(Illust, on_delete=models.CASCADE, verbose_name='対象記事')
    is_public = models.BooleanField('Public Comment?', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]