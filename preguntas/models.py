from django.db import models


#Modelo de creacion de usuario
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    usuario = models.CharField(max_length=45)
    contrasenia = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

#modelo para crear preguntas --- este va relacionado con usuario
class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=240)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_id_usuario')  # Field name made lowercase.
    
    def __str__(self):
        return self.pregunta

#modelo para crear Respuesta --- este va relacionado con persona(usuario invitado)

class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=240)
    pregunta_id_pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='PREGUNTA_id_pregunta')  # Field name made lowercase.
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_id_persona')  # Field name made lowercase.
    
    def __str__(self):
        return self.respuesta

#modelo para crear Persona --- Usuario que llenará los forms
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
