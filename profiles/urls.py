from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ProfileViewSet

router = SimpleRouter()
router.register("profiles", ProfileViewSet, basename="profiles")
urlpatterns = [
    path("", include(router.urls)),
]
