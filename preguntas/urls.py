from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from .views import preguntas_list, Respuesta_list, Persona_list, Usuario_list, preguntas_detail, Respuesta_detail, Persona_detail, Usuario_detail


urlpatterns = [
    path('listarPregunta/', preguntas_list),#mostrar Lista de preguntas
    path('listarPregunta/<int:pk>', preguntas_detail),# Crear editar y eliminar preguntas
    path('listarUsuario/', Usuario_list),# muestra la lista de usuarios
    path('listarUsuario/<int:pk>', Usuario_detail),#Crear Editar y Eliminar un Usuario
    path('listarRespuesta/', Respuesta_list), #Lista para mostrar Respuestas
    path('listarPersona/', Persona_list), # Lista para mostrar Usuarios que llenan form
]

