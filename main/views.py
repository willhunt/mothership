from django.shortcuts import render
from logIOT.models import Device
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'logIOT/index.html'

    def get_queryset(self):
        public_devices = Device.objects.filter(public=True)
        return  public_devices


def about(request):
    template_name = 'main/about.html'
    return render(request, template_name)

