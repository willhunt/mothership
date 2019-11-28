from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse


class SensorType(models.Model):
    ''' Sensor types and unit information allowing conversion '''
    sensor_type = models.CharField(max_length=50)

    def __str__(self):
        return self.sensor_type


class SensorOption(models.Model):
    ''' Sensor types and unit information allowing conversion '''
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    units = models.CharField(max_length=15)
    base_unit = models.BooleanField(default=False) # Indicate if base unit
    base_multiplier = models.FloatField(default=0) # Converison multiplier to base unit
    base_offset = models.FloatField(default=0) # Converison offset to base unit

    def __str__(self):
        return self.units


class Device(models.Model):
    ''' Device that can have multiple sensors '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        ''' Returns absolute url using primary key keyword argument '''
        return reverse('logIOT:device-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Channel(models.Model):
    ''' Device channel '''
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    units = models.ForeignKey(SensorOption, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        ''' Returns absolute url using primary key keyword argument '''
        return reverse('logIOT:channel-detail', kwargs={'pk': self.pk})


class Data(models.Model):
    ''' Channel Data '''
    # Get channel
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    value = models.FloatField()

    def __str__(self):
        return self.channel.name + ': Data'









