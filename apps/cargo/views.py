from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from utils.mixin import UltraModelMixin
from utils.permitions import IsOwner
from .models import Trek
from .serializers import *


class TrackAPIView(UltraModelMixin):
    queryset = Trek.objects.all()
    lookup_field = "id"
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ["number_trek", "description", "status"]
    ordering = ["status", "create_dt", "update_dt"]
    serializer_classes = {
        "list": ListTrekSerializer,
        "retrieve": RetrieveTrekSerializer,
        "create": CreateTrekSerializer,
        "update": CreateTrekSerializer,
    }
    permission_classes_by_active = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, IsOwner | IsAdminUser],
        "update": [IsAuthenticated, IsOwner | IsAdminUser],
    }
