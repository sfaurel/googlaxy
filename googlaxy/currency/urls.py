from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('settings/items', views.itemsSettings, name='items'),
    path('settings/numerals', views.numeralsSettings, name='numerals'),
]
