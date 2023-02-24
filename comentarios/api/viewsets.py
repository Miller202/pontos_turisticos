from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer

class ComentariosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing pontos turisticos.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
