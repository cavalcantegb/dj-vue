from rest_framework import routers
from estabelecimentos.viewsets import EstabelecimentoViewSet

router = routers.DefaultRouter()
router.register(r'estabelecimento', EstabelecimentoViewSet)