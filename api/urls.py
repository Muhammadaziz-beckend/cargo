from django.urls import path, include
from rest_framework.routers import DefaultRouter

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
    # track
    path("track/<int:id>/archived", DeleteTrackAPIView.as_view()),
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
