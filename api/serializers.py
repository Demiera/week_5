from rest_framework import serializers
from user.models import User, Topic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'picture'
        ]

class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
