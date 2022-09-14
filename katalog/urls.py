# TODO: Implement Routings Here
from django.urls import path
from katalog.views import lihat_katalog

app_name = 'katalog'

urlpatterns = [
    path('', lihat_katalog, name='lihat_katalog')
]