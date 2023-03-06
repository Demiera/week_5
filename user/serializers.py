from rest_framework import serializers
from .models import User, Topic
from api.serializers import UserPublicSerializer


class TopicsSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = [
            'owner',
            'name',
            'created',
            'update',
        ]

    def validate(self, attrs):
        return attrs


class UserSerializer(serializers.ModelSerializer):
    topic_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'picture',
            'topic_count',
        ]

    def get_topic_count(self, obj):
        return obj.topic_set.count()
