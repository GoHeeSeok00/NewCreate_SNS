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
