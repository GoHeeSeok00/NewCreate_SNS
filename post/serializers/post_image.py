from rest_framework import serializers

from post.models import PostImageModel


class PostImageSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 이미지 등록 시리얼라이저입니다.
    """

    class Meta:
        model = PostImageModel
        fields = [
            "image",
        ]

    def create(self, validated_data):
        """
        self.context["post"] : 게시글 오브젝트 id
        """
        instance = PostImageModel(**validated_data)
        instance.post_id = self.context["post"]
        instance.save()
        return instance
