from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('group.urls')),
    url(r'^', include('user.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', TokenVerifyView.as_view(), name='token_verify'),
]
