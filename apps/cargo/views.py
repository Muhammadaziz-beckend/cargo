from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

from utils.mixin import UltraModelMixin
from utils.permitions import IsOwner
from .models import Trek, Store
from .serializers import *


class TrackViewSet(UltraModelMixin):
    queryset = Trek.objects.filter(is_archived=False)
    queryset_obj_true = Trek.objects.filter(is_archived=True)
    lookup_field = "id"
    http_method_names = ["get", "post", "put", "patch"]
    search_fields = ["number_trek", "description"]
    ordering = ["create_dt", "update_dt"]
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    serializer_classes = {
        "list": ListTrekSerializer,
        "retrieve": RetrieveTrekSerializer,
        "create": CreateTrekSerializer,
        "update": UpdateTrekSerializer,
    }
    permission_classes_by_active = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, IsOwner | IsAdminUser],
        "update": [IsAuthenticated, IsOwner | IsAdminUser],
    }

    @action(["GET"], False, "archived")
    def get_all_archived(self, request, *args, **kwargs):
        queryset = self.queryset_obj_true
        serializers = ListTrekSerializer(queryset, many=True)
        return Response(serializers.data)


class DeleteTrackAPIView(APIView):
    queryset = Trek.objects.filter(is_archived=False)

    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(self.queryset, id=id)
        serializers = RetrieveTrekSerializer(queryset)
        return Response(serializers.data)

    def post(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(self.queryset, id=id)
        queryset.is_archived = True
        queryset.save()
        return Response(
            {"message": "Трек-код успешно удален!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, id, *args, **kwargs):

        return Response({"asd": id})


class StoreViewSet(UltraModelMixin):
    queryset = Store.objects.all()
    lookup_field = "id"
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    serializer_classes = {
        "list": ListStoreSerializer,
        "retrieve": RetrieveStoreSerializer,
        "create": CreateStoreSerializer,
        "update": CreateStoreSerializer,
    }
    permission_classes_by_active = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, IsAdminUser],
        "update": [IsAuthenticated, IsAdminUser],
    }
