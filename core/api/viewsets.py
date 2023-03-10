from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing pontos turisticos.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
