from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Member


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(default='NORMAL')
    username = serializers.CharField(max_length=20, required=True,
                                     validators=[UniqueValidator(queryset=Member.objects.all())])
    nickname = serializers.CharField(max_length=50, required=True,
                                     validators=[UniqueValidator(queryset=Member.objects.all())])
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    class Meta:
        model = Member

        fields = (
            'username',
            'nickname',
            'password',
            'user_type'
        )

    def create(self, validated_data):
        user = Member(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user