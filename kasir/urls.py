from django.contrib import admin
from django.urls import path, include
from kasir.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('barang/', include('barang.urls')),
]
