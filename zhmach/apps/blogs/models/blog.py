from django.conf import settings
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blogs:blog-detail', kwargs={'pk': self.pk})
