# minhaapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .cpf import CPF

class CPFCreate(APIView):
    def get(self, request):
        cpf_tool = CPF()
        estado = request.query_params.get("estado")
        if estado:
            cpf_data = cpf_tool.gerar_cpf(estado)
        else:
            cpf_data = cpf_tool.gerar_cpf()
        if not cpf_data:
            return Response({"mensagem":f"Estado '{estado}' não existe. Informe um estado válido"}, status=400)
        return Response(cpf_data, status=200)
    
class CPFValidate(APIView):
    def get(self, request):
        cpf_tool = CPF()
        cpf = request.query_params.get("cpf")
        if cpf:
            cpf_data = cpf_tool.validar_cpf(cpf)
            print(cpf_data)
            return Response(data=cpf_data, status=200)
        return Response({
            "mensagem":"parâmetro ?cpf=<cpf> necessário para validação.",
            "exemplo":"http://127.0.0.1:8000/cpf/validar/?cpf=94728067831"
            }, status=400)