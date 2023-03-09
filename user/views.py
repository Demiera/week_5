from rest_framework import generics, permissions, authentication
from rest_framework.exceptions import PermissionDenied

from user.models import User, Topic
from .serializers import TopicsSerializer, UserSerializer, RegisterSerializers




class ReadAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Topic.objects.filter(owner=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicsSerializer


class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class CanUpdateUserData(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.username == request.user.username


class UserRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if user.username != request.user.username:
            raise PermissionDenied('Cannot Update this Data')
        return super().update(request, *args, **kwargs)



class UserRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
