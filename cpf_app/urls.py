# minhaapp/urls.py
from django.urls import path
from .views import CPFView

urlpatterns = [
    path('', CPFView.as_view(), name='gerar-cpf'),
]