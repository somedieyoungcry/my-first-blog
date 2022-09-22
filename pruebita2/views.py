from django.shortcuts import render
from .models import post3
# Create your views here.

def muestra_datos(request):
    consulta = post3.objects.all()
    contexto = {'data': consulta}
    return render(request, 'inhtml/list_float.html', contexto)