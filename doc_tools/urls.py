from django.contrib import admin
from django.urls import path, include  # Importe 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cpf/', include('cpf_app.urls')),
]
