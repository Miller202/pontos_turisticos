from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing atracoes.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
