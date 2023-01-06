from django.contrib import admin
from .models import ShortUrl


@admin.register(ShortUrl)
class AdminShortUrl(admin.ModelAdmin):
    list_display = ('url', 'created_at')
    list_display_links = ('url',)