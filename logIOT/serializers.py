from rest_framework import serializers
from .models import Device, Data
from django.contrib.auth.models import User

# Serializers convert data (in the case Models) in JSON

class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Device
        fields = ('name', 'latitude', 'longitude', 'user')
        # Can send all:
        #fields = '__all_'


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('channel', 'log_time', 'value')


class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices')