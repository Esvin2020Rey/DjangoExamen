from rest_framework import serializers
from .models import Pregunta
from .models import Respuesta
from .models import Persona
from .models import Usuario

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id_pregunta',
            'pregunta',
            'usuario_id_usuario',
        )
        model = Pregunta

class RespuestasSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id_respuesta',
            'respuesta',
            'pregunta_id_pregunta',
            'persona_id_persona',
        )
        model = Respuesta


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id_persona',
            'nombre',
            'apellido',
        )
        model = Persona

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id_usuario',
            'nombre',
            'apellido',
            'usuario',
            'contrasenia'
        )
        model = Usuario
