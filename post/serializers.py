from rest_framework import serializers

from post.models import Post as PostModel


class PostListSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.21

    게시글 목록 조회를 위한 시리얼라이저입니다.
    """

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = PostModel
        fields = [
            "user",
            "status",
            "title",
            "content",
            "hashtags_text",
            "view_count",
            "like_count",
        ]
