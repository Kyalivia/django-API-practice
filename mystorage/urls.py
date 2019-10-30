# 라우터 기반
from rest_framework.routers import  DefaultRouter
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImageViewSet)
router.register('files', views.FileViewSet)

# 'set' object is not reversible
# urlpatterns 괄호 에러
urlpatterns = [
    path('', include(router.urls)),
]