from rest_framework import serializers

from post.models import Post as PostModel


class PostSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.21

    게시글 목록 조회를 위한 시리얼라이저입니다.
    """

    class Meta:
        model = PostModel
        fields = []
