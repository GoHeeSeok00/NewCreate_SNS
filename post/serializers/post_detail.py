from rest_framework import serializers

from post.models import PostModel


class PostDetailGetSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 상세 조회를 위한 시리얼라이저입니다.
    """

    user = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    def get_status(self, obj):
        return obj.status.status

    class Meta:
        model = PostModel
        fields = [
            "id",
            "user",
            "title",
            "content",
            "hashtags_text",
            "like_count",
            "view_count",
            "status",
        ]


class PostDetailUpdateSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 수정을 위한 시리얼라이저입니다.
    """

    class Meta:
        model = PostModel
        fields = [
            "title",
            "content",
            "hashtags_text",
        ]

    def update(self, instance, validated_data):
        """
        모든 필드를 수정하는게 아니라 입력된 필드 + updated_at 필드만 수정
        """
        field_list = ["updated_at"]
        for key, value in validated_data.items():
            setattr(instance, key, value)
            field_list.append(key)
        instance.save(update_fields=field_list)
        return instance
