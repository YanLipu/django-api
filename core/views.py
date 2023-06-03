from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario, Grupo
from .serializers import UsuarioSerializer, GrupoSerializer

@api_view(['GET'])
def getGrupos(request):
    print('request', request)
    grupos = Grupo.objects.all()
    serializer = GrupoSerializer(grupos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    serializer = UsuarioSerializer(usuario, many=False)
    return Response(serializer.data)

# Create your views here.
