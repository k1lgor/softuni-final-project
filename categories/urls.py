from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet

router = SimpleRouter()
router.register("categories", CategoryViewSet, basename="categories")
urlpatterns = [
    path("", include(router.urls)),
]
