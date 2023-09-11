from django.shortcuts import render

def homepage(request):
    return render(request, "cpf_gui/index.html")