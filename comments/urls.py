from django.urls import include, path
from rest_framework.routers import SimpleRouter


from .views import CommentViewSet

router = SimpleRouter()

router.register("comments", CommentViewSet, basename="comments")
urlpatterns = [
    path("", include(router.urls)),
]
