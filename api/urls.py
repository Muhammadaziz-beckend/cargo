from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.account.views import Login, Logout, Register
from apps.cargo.views import TrackAPIView
from .ysge import swagger

router = DefaultRouter()
router.register("track", TrackAPIView)

urlpatterns = [
    # auth
    path("auth/register/", Register.as_view()),
    path("auth/login/", Login.as_view()),
    path("auth/logout", Logout.as_view()),
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
