from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/groups/$', views.group_list),
    url(r'^api/groups/([0-9]+)$', views.group_detail),
]