from django.shortcuts import render
from services.models import Service

def service_index(request):
    services = Service.objects.all()
    context = {
        'services' = services #service or services
    }
    return render(request, 'service_index.html', context)

def service_detail(request, pk): #primary key
    service = Service.objects.get(pk=pk)
    context = {
        'service': service #service or services
    }
    return render(request, 'service_detail.html', context)
# Create your views here.
