from rest_framework import generics
from user.models import User, Topic
from .serializers import UserSerializer


class ReadAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



