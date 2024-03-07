from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import *

router = DefaultRouter()
router.register('personapi', ModelViewSetview, basename='person')
router.register('personapi1', ModelViewReadOnlyViewSet, basename='person1')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
