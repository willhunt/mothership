from django.contrib import admin

from .models import Device, Channel, Data, SensorOption, SensorType

admin.site.register(Device)
admin.site.register(Channel)
admin.site.register(Data)
admin.site.register(SensorType)
admin.site.register(SensorOption)
