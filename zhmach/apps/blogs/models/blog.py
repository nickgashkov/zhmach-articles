from django.conf import settings
from django.db import models
from django.db.models import F
from django.urls import reverse


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания',
    )
    name = models.CharField(
        max_length=500,
        verbose_name='Наименование',
    )
    image = models.ImageField(
        upload_to='%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blogs:blog-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('blogs:blog-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('blogs:blog-delete', kwargs={'pk': self.pk})

    def increment_views(self):
        self.views = F('views') + 1
        self.save()
