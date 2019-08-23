from rest_framework import routers
from api.estabelecimentos.viewsets import EstabelecimentoViewSet

router = routers.DefaultRouter()
router.register(r'estabelecimento', EstabelecimentoViewSet)