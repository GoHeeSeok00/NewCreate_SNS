from django.db.models import F
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from post.models import PostLikeModel, PostModel


class PostLikeSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요를 위한 serializer입니다.
    사용자는 한 게시글에 하나의 좋아요만 할 수 있어 UniqueTogetherValidator를 사용해서 중복체크를 합니다.
    """

    class Meta:
        model = PostLikeModel
        fields = ["user", "post"]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=PostLikeModel.objects.all(),
                fields=("user", "post"),
                message=_("이미 좋아요한 게시글입니다."),
            )
        ]

    def create(self, validated_data):
        """

        :param validated_data["user"]: 사용자 객체
        :param validated_data["post"]: 게시글 객체
        :return:
        """
        PostModel.objects.filter(id=validated_data["post"].id).update(
            like_count=F("like_count") + 1
        )
        instance = PostLikeModel(**validated_data)
        instance.save()
        return instance
