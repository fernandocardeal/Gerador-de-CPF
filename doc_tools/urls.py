from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cpf/', include('cpf_api.urls')),
    path('', include('cpf_gui.urls')),
]
