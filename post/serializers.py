from rest_framework import serializers

from post.models import Post as PostModel


class PostListSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.22

    게시글 목록 조회를 위한 시리얼라이저입니다.
    """

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = PostModel
        fields = [
            "id",
            "user",
            "status",
            "title",
            "content",
            "hashtags_text",
            "view_count",
            "like_count",
        ]


class PostSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.22

    게시글 등록을 위한 시리얼라이저입니다.
    """

    class Meta:
        model = PostModel
        fields = [
            "status",
            "title",
            "content",
            "hashtags_text",
        ]

    def validate(self, data):
        if data["status"] not in [1, 2]:  # public, private
            raise serializers.ValidationError("잘못된 입력입니다.")
        return data

    def create(self, validated_data):
        """
        self.context["user"] : request.user (로그인 유저 instance)
        """
        instance = PostModel(**validated_data)
        instance.user = self.context["user"]
        instance.save()
        return instance
