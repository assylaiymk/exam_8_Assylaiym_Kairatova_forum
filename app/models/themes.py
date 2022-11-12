from django.db import models
from django.utils import timezone

from app.managers import ThemeManager


class Theme(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=3000, null=False, blank=False)
    author = models.CharField(verbose_name='Author', max_length=100, null=False, blank=False, default='No name')
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)

    objects = ThemeManager()

    def __str__(self):
        return f'{self.title} - {self.author}'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
