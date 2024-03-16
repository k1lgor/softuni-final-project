from rest_framework import status, viewsets
from rest_framework.response import Response

from accounts.models import User
from .serializers import ProfileSerializer

from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Profile.objects.all()
        if username := self.request.query_params.get("username", None):
            user = User.objects.filter(username=username).first()
            queryset = queryset.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            if user.profile is not None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            profile = Profile.objects.create(user=user, **serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        serializer = self.get_serializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
