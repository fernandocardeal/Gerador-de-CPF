# minhaapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .cpf import CPF

class CPFCreate(APIView):
    def get(self, request):
        cpf_tool = CPF()
        estado = request.query_params.get('estado')
        if estado:
            cpf_data = cpf_tool.gerar_cpf(estado)
        else:
            cpf_data = cpf_tool.gerar_cpf()
        if not cpf_data:
            return Response({"mensagem":f"Estado '{estado}' não existe. Informe um estado válido"}, status=400)
        return Response(cpf_data, status=200)
