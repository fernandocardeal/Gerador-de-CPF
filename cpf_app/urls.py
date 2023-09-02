# minhaapp/urls.py
from django.urls import path
from .views import CPFCreate

urlpatterns = [
    path('gerar/', CPFCreate.as_view(), name='gerar-cpf'),
]