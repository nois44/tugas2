from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def lihat_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_barang_katalog, 
        'nama' : 'Gabriel Edgar Firdausyah Nugroho', 
        'npm' : '2106752312'
    }
    return render(request, 'katalog.html', context)