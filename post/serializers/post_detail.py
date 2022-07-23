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
