from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watch_list(request):
    data_watch_list = MyWatchList.objects.all()
    context = {
        'watch_list' : data_watch_list, 
        'nama' : 'Gabriel Edgar Firdausyah Nugroho', 
        'npm' : '2106752312'
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")
