from django.conf.urls import url
from django.contrib import admin
from .views import UserListView
from . import views

urlpatterns = [
    url(r'^api/users/registration$', UserListView.as_view(), name='create_user'),
    url(r'^api/users/([0-9]+)$', views.user_detail),
    url(r'^api/users/', views.users_list)  
]   