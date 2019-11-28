from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Device, Channel
from .serializers import DeviceSerializer, DataSerializer
from .forms import DeviceForm, ChannelForm
from .permissions import IsOwnerOrReadOnly


class DevicesView(generic.ListView):
    template_name = 'logIOT/devices.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Device.objects.filter(user=user)
        else:
            return Device.objects.filter(public=True)


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'logIOT/device_detail_MDL.html'


class DeviceFormView(View):
    # Choose form blueprint
    form_class = DeviceForm # Use form created in forms.py
    template_name = 'logIOT/device_form.html'

    # Display blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Create user object from form but not saved to database
            new_device = form.save(commit=False)
            # Clean and normalise data
            new_device.name = form.cleaned_data['name']
            new_device.description = form.cleaned_data['description']
            new_device.latitude = form.cleaned_data['latitude']
            new_device.longitude = form.cleaned_data['longitude']
            new_device.image = form.cleaned_data['image']
            new_device.user = request.user
            new_device.save()
            return redirect(new_device)

        return render(request, self.template_name, {'form': form})


class DeviceUpdateView(UpdateView):
    # Automatically will render <modelname>_form.html
    model = Device
    form_class = DeviceForm

    def get_object(self, queryset=None):
        # Hook to ensure object is owned by request.user
        object = super(DeviceUpdateView, self).get_object()
        if not object.user == self.request.user:
            raise Http404
        return object


class DeviceDeleteView(DeleteView):
    model= Device
    success_url = reverse_lazy('main:index')

    def get_object(self, queryset=None):
        # Hook to ensure object is owned by request.user
        object = super(DeviceDeleteView, self).get_object()
        if not object.user == self.request.user:
            raise Http404
        return object


class ChannelDetailView(generic.DetailView):
    model = Channel
    template_name = 'logIOT/channel_detail_MDL.html'


class ChannelFormView(View):
    # Choose form blueprint
    form_class = ChannelForm # Use form created in forms.py
    template_name = 'logIOT/channel_form.html'

    # Display blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Create user object from form but not saved to database
            new_channel = form.save(commit=False)
            # Clean and normalise data
            new_channel.name = form.cleaned_data['name']
            new_channel.sensor_type = form.cleaned_data['sensor_type']
            new_channel.units = form.cleaned_data['units']
            # Get device id, if none choose ''
            new_channel.device = Device.objects.get(pk=request.GET.get('device_id', ''))
            new_channel.save()
            return redirect(new_channel)

        return render(request, self.template_name, {'form': form})


class ChannelUpdateView(UpdateView):
    # Automatically will render <modelname>_form.html
    model = Channel
    form_class = ChannelForm

    def get_object(self, queryset=None):
        # Hook to ensure channel's device is owned by request.user
        object = super(ChannelUpdateView, self).get_object()
        if not object.device.user == self.request.user:
            raise Http404
        return object


class ChannelDeleteView(DeleteView):
    model= Channel
    success_url = reverse_lazy('main:index')

    def get_object(self, queryset=None):
        # Hook to ensure channel's device is owned by request.user
        object = super(ChannelDeleteView, self).get_object()
        if not object.device.user == self.request.user:
            raise Http404
        return object


class ApiDeviceList(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApiDataLogging(APIView):
    ''' Adds data for device channel via API '''
    # For api data loggong use api token to authenticate
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndexView(View):
    template_name = 'logIOT/index.html'

    def get_queryset(self):
        public_devices = Device.objects.filter(public=True)
        return  public_devices


class DashboardView(View):
    template_name = 'logIOT/dashboard.html'








