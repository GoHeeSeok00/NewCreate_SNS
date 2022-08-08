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
            "id",
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
            "id",
            "email",
            "password",
            "password_check",
            "nickname",
            "username",
            "introduce",
            "mobile_number",
            "date_of_birth",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            },
        }
        read_only_fields = ["id"]

    def validate(self, data):
        """
        비밀번호 더블체크 validate

        :param data:  1차 validate를 통과한 데이터
        :return data: 커스텀 validate를 통과한 데이터
        """
        password = data.get("password", "")
        password_check = data.get("password_check", "")

        if password != password_check:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return data

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue

            setattr(instance, key, value)
        instance.save()
        return instance


class UserWithdrawSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.22

    회원 탈퇴를 위한 시리얼라이저입니다.
    """

    class Meta(object):
        model = UserModel
        fields = [
            "is_active",
        ]

    def validate(self, data):
        if data["is_active"] != False:
            raise serializers.ValidationError("잘못된 입력입니다.")
        return data

    def update(self, instance, validated_data):
        """
        입력된 필드만 수정
        is_active = False | 회원 탈퇴
        """
        field_list = []
        for key, value in validated_data.items():
            setattr(instance, key, value)
            field_list.append(key)
        instance.save(update_fields=field_list)
        return instance
