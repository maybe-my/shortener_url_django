from django.forms import ModelForm
from .models import ShortUrl


class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['url',]