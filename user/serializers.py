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

    def to_representation(self, instance):
        user = self.context['request'].user
        picture = self.context['request'].build_absolute_uri(instance.picture)
        if user == instance:
            return super().to_representation(instance)
        else:
            return {
                'last_name': instance.last_name,
                'picture': picture or None
            }
    def get_topic_count(self, obj):
        return obj.topic_set.count()


class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
            'picture',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'password not match.'})
        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        last_name = validated_data.get('last_name', username)
        user = User.objects.create(
            username=username,
            first_name=validated_data['first_name'],
            last_name=last_name,
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
