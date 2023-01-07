from django.forms import ModelForm, TextInput
from .models import ShortUrl


class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['url',]
        widgets = {
            'url': TextInput(attrs={
                'class': "form-control form-control-lg flex-shrink-1 form-control-borderless",
                'placeholder': 'Enter the link here',
                'id': 'url-input',
                'autocomplete': 'off'
            })
        }