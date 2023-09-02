# minhaapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .cpf import CPF

class CPFView(APIView):
    def get(self, request):
        cpf_tool = CPF()
        estado = request.query_params.get('estado')
        
        if estado:
            cpf_nao_formatado = cpf_tool.cpf_generator(estado)
        else:
            cpf_nao_formatado = cpf_tool.cpf_generator()

        cpf_formatado = cpf_tool.cpf_formatter(cpf_nao_formatado)
        data = {
            0: cpf_nao_formatado,
            1: cpf_formatado,
        }

        return Response(data)
