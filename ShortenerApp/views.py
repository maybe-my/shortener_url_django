from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, RedirectView, DetailView
from .models import ShortUrl
from .forms import ShortUrlForm


class IndexView(CreateView):
    model = ShortUrl
    form_class = ShortUrlForm
    template_name = 'ShortenerApp/create.html'


class RedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        page = get_object_or_404(ShortUrl, short_url=kwargs.get('short_url'))
        page.count_visits += 1
        page.save()
        return page.get_redirect_url()


class SuccessView(DetailView):
    slug_url_kwarg = 'short_url'
    slug_field = 'short_url'
    model = ShortUrl
    template_name = 'ShortenerApp/success.html'
