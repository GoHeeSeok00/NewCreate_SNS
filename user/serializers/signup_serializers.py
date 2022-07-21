from rest_framework import serializers

from user.models import User as UserModel


class UserSignupSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.21

    회원가입을 위한 시리얼라이저입니다.
    """

    password_check = serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta(object):
        model = UserModel
        fields = [
            "email",
            "password",
            "password_check",
            "nickname",
            "username",
            "mobile_number",
            "date_of_birth",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            },
        }

    def create(self, validated_data):
        """
        :param validated_data: validate를 통과한 data
        :key password_check:   user 인스턴스를 만들 때 필요없는 필드는 제거합니다.
        :key password:         set_password 함수를 이용해 암호 해싱
        :return instance:      UserModel instance
        """
        validated_data.pop("password_check", "")
        password = validated_data.pop("password", "")

        instance = UserModel(**validated_data)

        instance.set_password(password)
        instance.save()

        return instance

    def validate(self, data):
        """
        비밀번호 더블체크 validate

        :param data:    1차 validate를 통과한 데이터
        :return data:   커스텀 validate를 통과한 데이터
        """
        password = data.get("password", "")
        password_check = data.get("password_check", "")

        if password != password_check:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")

        return data
