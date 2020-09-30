from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, permissions
from .models import Pregunta, Respuesta, Persona, Usuario
from .serializers import PreguntasSerializer, RespuestasSerializer, PersonaSerializer, UsuarioSerializer


@api_view(['GET', 'POST'])

def preguntas_list(request):
    if request.method == 'GET':
        data = Pregunta.objects.all()

        serializer = PreguntasSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PreguntasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def preguntas_detail(request, pk):
    try:
        vartodo = Pregunta.objects.get(pk=pk)
    except Pregunta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PreguntasSerializer(vartodo, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vartodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

    # ---------METODOS PARA LA TABLA DE RESPUESTA-----------------------------
#--------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def Respuesta_list(request):
    if request.method == 'GET':
        data = Respuesta.objects.all()

        serializer = RespuestasSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RespuestasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def Respuesta_detail(request, pk):
    try:
        vartodo = Respuesta.objects.get(pk = pk)
    except Respuesta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RespuestasSerializer(vartodo, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vartodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------METODOS PARA LA TABLA DE PERSONA-----------------------------
#--------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def Persona_list(request):
    if request.method == 'GET':
        data = Persona.objects.all()

        serializer = PersonaSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def Persona_detail(request, pk):
    try:
        vartodo = Persona.objects.get(pk = pk)
    except Persona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonaSerializer(vartodo, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vartodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------METODOS PARA LA TABLA DE USUARIO-----------------------------
#--------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def Usuario_list(request):
    if request.method == 'GET':
        data = Usuario.objects.all()

        serializer = UsuarioSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def Usuario_detail(request, pk):
    try:
        vartodo = Usuario.objects.get(pk = pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UsuarioSerializer(vartodo, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vartodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)