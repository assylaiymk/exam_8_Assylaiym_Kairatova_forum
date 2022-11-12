from django.db import models

from app.models import Theme


class Reply(models.Model):
    theme = models.ForeignKey(Theme, verbose_name='Theme', related_name='themes', on_delete=models.CASCADE)
    author = models.CharField(
        verbose_name='Author',
        null=True,
        default='Anonymous',
        max_length=40
    )
    text = models.TextField(
        verbose_name='Reply',
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
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
