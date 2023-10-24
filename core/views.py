from django.shortcuts import render
from .models import Comunicado, Entidades

def home(request):
    title = "Comunicados | UTFSM"
    filtrar_entidad = request.GET.get("Departamento")
    entidades = Entidades.objects.all()
    
    # Muestra comunicados según selección

    if filtrar_entidad and filtrar_entidad != "Departamento":
        comunicados = Comunicado.objects.filter(entidad__nombre=filtrar_entidad, visible=True).order_by('-fecha_publicacion')
    # Muestra todos los comunicados
    else:
        comunicados = Comunicado.objects.filter(visible=True).order_by('-fecha_publicacion')

    data = {
        "title": title,
        "comunicados": comunicados,
        "entidades": entidades,
        "filtrar_entidad": filtrar_entidad,
    }

    return render(request, 'core/index.html', data)
