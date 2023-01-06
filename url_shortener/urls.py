from django.contrib import admin
from django.urls import path
from ShortenerApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='create'),
    path('success/<slug:short_url>/', views.SuccessView.as_view(), name='detail'),
    path('<slug:short_url>/', views.RedirectView.as_view(), name='redirect'),
]
