from django.db import transaction
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
        fields = ["user", "post", "is_like"]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=PostLikeModel.objects.all(),
                fields=("user", "post"),
                message=_("이미 좋아요한 게시글입니다."),
            )
        ]

    @transaction.atomic
    def create(self, validated_data):
        """
        :param validated_data["user"]: 사용자 객체
        :param validated_data["post"]: 게시글 객체
        """
        PostModel.objects.filter(id=validated_data["post"].id).update(
            like_count=F("like_count") + 1
        )
        instance = PostLikeModel(**validated_data)
        instance.save()
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        :param validated_data["user"]:      사용자 객체
        :param validated_data["post"]:      게시글 객체
        :param validated_data["is_like"]:   좋아요 여부

        모든 필드를 수정하는게 아니라 입력된 필드 + updated_at 필드만 수정
        """
        if instance.is_like == True:
            raise serializers.ValidationError({"error": "이미 좋아요 한 게시글입니다."})

        PostModel.objects.filter(id=validated_data["post"].id).update(
            like_count=F("like_count") + 1
        )

        validated_data.pop("user")
        validated_data.pop("post")

        field_list = ["updated_at"]
        for key, value in validated_data.items():
            setattr(instance, key, value)
            field_list.append(key)
        instance.save(update_fields=field_list)
        return instance


class PostUnLikeSerializer(serializers.ModelSerializer):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요 취소를 위한 serializer입니다.
    """

    class Meta:
        model = PostLikeModel
        fields = ["user", "post", "is_like"]

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        :param validated_data["user"]:      사용자 객체
        :param validated_data["post"]:      게시글 객체
        :param validated_data["is_like"]:   좋아요 여부

        모든 필드를 수정하는게 아니라 입력된 필드 + updated_at 필드만 수정
        """
        if instance.is_like == False:
            raise serializers.ValidationError({"error": "이미 좋아요 취소가 된 게시글입니다."})

        PostModel.objects.filter(id=validated_data["post"].id).update(
            like_count=F("like_count") - 1
        )

        validated_data.pop("user")
        validated_data.pop("post")

        field_list = ["updated_at"]
        for key, value in validated_data.items():
            setattr(instance, key, value)
            field_list.append(key)
        instance.save(update_fields=field_list)
        return instance
