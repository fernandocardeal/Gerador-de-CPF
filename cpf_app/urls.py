# minhaapp/urls.py
from django.urls import path
from .views import CPFCreate, CPFValidate

urlpatterns = [
    path("gerar/", CPFCreate.as_view(), name="gerar-cpf"),
    path("validar/", CPFValidate.as_view(), name="validar-cpf")
]