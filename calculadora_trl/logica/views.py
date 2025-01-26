from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Modelo, Pregunta, Respuesta, Nivel

def seleccionar_modelo(request):
    modelos = Modelo.objects.all()
    return render(request, 'seleccionar_modelo.html', {'modelos': modelos})

def obtener_pregunta(request):
    if request.method == 'GET':
        pregunta_id = request.GET.get('pregunta_id')
        pregunta = Pregunta.objects.get(id=pregunta_id)
        respuestas = Respuesta.objects.filter(pregunta=pregunta)
        data = {
            'pregunta': pregunta.texto,
            'respuestas': [{'id': r.id, 'texto': r.texto} for r in respuestas]
        }
        return JsonResponse(data)

def preguntas(request):
    if request.method == 'POST':
        modelo_id = request.POST.get('modelo')
        modelo = Modelo.objects.get(nombre=modelo_id)
        preguntas = Pregunta.objects.filter(modelo=modelo).order_by('numero')
        return render(request, 'preguntas.html', {'modelo': modelo, 'preguntas': preguntas})
    return redirect('seleccionar_modelo')

def calcular_resultado(request):
    if request.method == 'POST':
        modelo_id = request.POST.get('modelo')
        modelo = Modelo.objects.get(nombre=modelo_id)
        
        puntos_totales = 0
        for key, value in request.POST.items():
            if key.startswith('pregunta_'):
                respuesta = Respuesta.objects.get(id=value)
                puntos_totales += respuesta.puntos
        
        nivel = Nivel.objects.filter(modelo=modelo, ptos_necesarios__lte=puntos_totales).order_by('-ptos_necesarios').first()
        
        return render(request, 'resultado.html', {
            'nivel': nivel,
            'puntos_totales': puntos_totales,
            'modelo': modelo
        })
    return redirect('seleccionar_modelo')

def obtener_puntos(request):
    if request.method == 'GET':
        respuesta_id = request.GET.get('respuesta_id')
        respuesta = Respuesta.objects.get(id=respuesta_id)
        return JsonResponse({'puntos': respuesta.puntos})
    
def custom_server_error(request):
    tipo = "500"
    return render(request, "vista_error.html", {'tipo': tipo})

def custom_bad_request(request, exception):
    tipo = "404"
    exception = str(exception)
    return render(request, "vista_error.html", {'tipo': tipo, 'exception': exception})

def custom_csrf_failure(request):
    tipo = "de CRSF"
    return render(request, "vista_error.html", {'tipo': tipo})