from rest_framework import viewsets
from .models import Estabelecimento
from .serializers import EstabelecimentoSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer