from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personlistcreate/<int:pk>/', PersonListCreate.as_view()),
    path('personretupdes/<int:pk>/', PersonRetDestroy.as_view()),
]
