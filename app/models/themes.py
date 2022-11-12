from django.db import models
from django.utils import timezone

from app.managers import ArticleManager


class Theme(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=3000, null=False, blank=False)
    author = models.CharField(verbose_name='Author', max_length=100, null=False, blank=False, default='No name')
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)

    objects = ArticleManager()

    def __str__(self):
        return f'{self.title} - {self.author}'


class Reply(models.Model):
    theme = models.ForeignKey(Theme, verbose_name='Theme', related_name='replies', on_delete=models.CASCADE)
    author = models.CharField(
        verbose_name='Author',
        null=True,
        default='Anonymous',
        max_length=40
    )
    text = models.TextField(
        verbose_name='Replies',
        max_length=400
    )
    created_at = models.DateTimeField(
        verbose_name='Date created',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Date updated',
        auto_now=True
    )

    def __str__(self):
        return f"{self.author} : {self.text[:30]}"

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
        permissions = [
            ('any_data', 'Anything')
        ]

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
