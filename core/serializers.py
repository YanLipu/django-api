from rest_framework import serializers
from .models import Grupo, Usuario

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    # grupo = GrupoSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'


