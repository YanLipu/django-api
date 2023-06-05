from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Usuario, Grupo
from .serializers import UsuarioSerializer, GrupoSerializer

class UsuarioController(APIView):
    def get(self, request):
        print('request', request)
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):        
        usuario = self.get_object(id)
        if usuario is None:
            return Response(
                {"error": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        usuario = self.get_object(id)
        if usuario is None:
            return Response(
                {"error": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        usuario.delete()
        return Response(
                {"message": "Usuário excluido com sucesso."},
                status=status.HTTP_204_NO_CONTENT
            )

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return None

class GrupoController(APIView):
    def get(self,request):
        grupos = Grupo.objects.all()
        serializer = GrupoSerializer(grupos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        grupo = self.get_object(id)
        if grupo is None:
            return Response(
                {"error": "Grupo não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = GrupoSerializer(grupo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        grupo = self.get_object(id)
        if grupo is None:
            return Response(
                {"error": "Grupo não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        grupo.delete()
        return Response(
                {"message": "Grupo excluido com sucesso."},
                status=status.HTTP_204_NO_CONTENT
            )

    def get_object(self, pk):
        try:
            return Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return None
