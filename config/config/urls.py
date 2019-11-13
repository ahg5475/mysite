from django.contrib import admin
from django.urls import path, include
import dappajyeo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dappajyeo.views.index, name='home'),
    path('Dappajyeo/', include('dappajyeo.urls')),
]
