from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)

    def __str__(self):
      return self.name

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
      return self.name

class Post(models.Model):
    title = models.CharField('タイトル名', max_length=30)
    text = models.TextField('本文')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    created_at = models.DateTimeField('学習日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
      return self.title
