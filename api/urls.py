from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.account.views import Login, Logout, Register
from apps.cargo.views import DeleteTrackAPIView, StoreViewSet, TrackViewSet
from .ysge import swagger

router = DefaultRouter()
router.register("track", TrackViewSet)
router.register("store", StoreViewSet)

urlpatterns = [
    # auth
    path("auth/register/", Register.as_view()),
    path("auth/login/", Login.as_view()),
    path("auth/logout", Logout.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # /auth/
    # track
    path("track/<int:id>/archives/", DeleteTrackAPIView.as_view()),
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
