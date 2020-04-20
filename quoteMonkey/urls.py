from django.contrib import admin
from django.urls import path, include
from monkey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('monkey.urls')),
]
