from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'logIOT'

urlpatterns = [
    url(r'^$', views.DevicesView.as_view(), name='devices'),
    url(r'device/(?P<pk>[0-9]+)/$', views.DeviceDetailView.as_view(), name='device-detail'),
    url(r'device/add/$', views.DeviceFormView.as_view(), name='device-add'),
    url(r'device/(?P<pk>[0-9]+)/update/$', views.DeviceUpdateView.as_view(), name='device-update'),
    url(r'device/(?P<pk>[0-9]+)/delete/$', views.DeviceDeleteView.as_view(), name='device-delete'),
    url(r'api/devices/', views.ApiDeviceList.as_view(), name='api-devicelist'),
    url(r'channel/(?P<pk>[0-9]+)/$', views.ChannelDetailView.as_view(), name='channel-detail'),
    #url(r'channel/(?P<pk>[0-9]+)/data.plot$', plots.plotChannelData, name='channel-plot'),
    url(r'channel/add/$', views.ChannelFormView.as_view(), name='channel-add'),
    url(r'channel/(?P<pk>[0-9]+)/update/$', views.ChannelUpdateView.as_view(), name='channel-update'),
    url(r'channel/(?P<pk>[0-9]+)/delete/$', views.ChannelDeleteView.as_view(), name='channel-delete'),
    url(r'api/data/', views.ApiDataLogging.as_view(), name='api-datalogging'),
    url(r'dashboard/$', views.DashboardView.as_view(), name='dashboard'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
