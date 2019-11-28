from django.conf.urls import url
from . import views

app_name = 'userControl'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'modify/(?P<pk>[0-9]+)/$', views.UserUpdateView.as_view(), name='user-update'),
    url(r'modify/(?P<pk>[0-9]+)/delete/$', views.UserDeleteView.as_view(), name='user-delete'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^(?P<username>\w+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^obtain-api-token/$', views.CreateApiTokenView.as_view(), name='apitoken-create'),
]
