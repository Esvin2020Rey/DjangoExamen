from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from preguntas.models import Usuario


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('usuario',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
#5555555
#22525
    def create(self, validated_data):
        password = validated_data.pop('contrasenia', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = Usuario
        fields = ('token', 'usuario', 'contrasenia')