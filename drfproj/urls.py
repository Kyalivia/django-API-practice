from django.contrib import admin
from django.urls import path, include
from mystorage import urls
# 로그인 로그아웃 기능
from rest_framework import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    # 로그인 로그아웃 기능
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, doucument_root=settings.MEDIA_ROOT)