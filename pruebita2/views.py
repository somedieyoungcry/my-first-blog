from django.shortcuts import render
from .models import post3
# Create your views here.

def flotantes(request):
    return render(request, 'pruebita2/flotantes.html', {'flotantes': post3.objects.all()})