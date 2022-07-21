from rest_framework import serializers

from user.models import User as UserModel


class UserListSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.22

    회원 목록 조회를 위한 시리얼라이저입니다.
    """

    class Meta(object):
        model = UserModel
        fields = [
            "nickname",
            "profile_image",
            "introduce",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.22

    회원 상세 조회, 정보 수정을 위한 시리얼라이저입니다.
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
