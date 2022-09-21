from django.urls import path
from mywatchlist.views import show_watch_list, show_xml, show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watch_list, name='show_watch_list'),
    path('html/', show_watch_list, name='show_watch_list'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json')
]
