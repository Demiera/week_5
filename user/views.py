from rest_framework import generics, permissions, authentication
from user.models import User, Topic
from .serializers import TopicsSerializer, UserSerializer, RegisterSerializers
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ReadAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Topic.objects.filter(owner=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicsSerializer


class UserListView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
