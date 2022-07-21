from rest_framework import serializers

from user.models import User as UserModel


class UserSignupSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석

    회원가입을 위한 시리얼라이저입니다.
    """

    class Meta(object):
        model = UserModel
        fields = [
            "email",
            "password",
            "nickname",
            "username",
            "mobile_number",
            "date_of_birth",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """
        :param validated_data: validate를 통과한 data
        :key password: set_password 함수를 이용해 암호 해싱
        :return instance: UserModel instance
        """
        password = validated_data.pop("password", "")

        instance = UserModel(**validated_data)

        instance.set_password(password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        """
        :param instance: 수정하려고 하는 instance
        :param validated_data: validate를 통과한 data
        :return instance: instance
        """
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()

        return instance
