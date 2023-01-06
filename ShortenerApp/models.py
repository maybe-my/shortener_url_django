import string
import random
from django.db import models
from django.urls import reverse


class ShortUrl(models.Model):
    url = models.URLField(blank=False, null=False)
    short_url = models.CharField(unique=True, max_length=10)
    count_visits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.short_url)])

    def save(self, *args, **kwargs):
        self.short_url = ''.join(random.choice(string.ascii_letters)
                                 for x in range(10))
        super(ShortUrl, self).save(*args, **kwargs)

    def get_redirect_url(self):
        return self.url