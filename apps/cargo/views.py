from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
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
    http_method_names = ["get", "post", "put", "patch", "delete"]
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

    def get_queryset(self):
        user = self.request.user

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )
        queryset = self.queryset.filter(owner=user).filter(is_archived=False)

        return queryset

    def get_queryset_obj_true(self):
        user = self.request.user

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )
        queryset = self.queryset.filter(owner=user).filter(is_archived=True)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["GET"], False, "archives")
    def get_all_archived(self, request, *args, **kwargs):
        queryset = self.get_queryset_obj_true()
        serializers = ListTrekSerializer(queryset, many=True)
        return Response(serializers.data)


class DeleteTrackAPIView(APIView):
    queryset = Trek.objects

    def get_queryset(self):
        user = self.request.user

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )
        queryset = self.queryset.filter(owner=user).filter(is_archived=True)

        return queryset

    def post(self, request, id, *args, **kwargs):

        track = get_object_or_404(self.get_queryset(), id=id)

        track.is_archived = False
        track.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


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
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAuthenticated, IsAdminUser],
        "update": [IsAuthenticated, IsAdminUser],
    }
