from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
import calculadora_trl.settings as settings
from . import views

urlpatterns = [
    path('', views.seleccionar_modelo, name='seleccionar_modelo'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('obtener_pregunta/', views.obtener_pregunta, name='obtener_pregunta'),
    path('obtener_puntos/', views.obtener_puntos, name='obtener_puntos'),
    path('calcular_resultado/', views.calcular_resultado, name='calcular_resultado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)