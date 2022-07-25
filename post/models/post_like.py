from django.db import models

from config.models import TimeStamp as TimeStampModel
from post.models.post import Post as PostModel
from user.models import User as UserModel


class PostLike(TimeStampModel):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요를 위한 모델입니다.

    unique constraints 설정으로 한 사용자가 한 게시글에 좋아요를 한번만 할 수 있습니다.
    """

    user = models.ForeignKey(
        to=UserModel,
        verbose_name="사용자",
        on_delete=models.CASCADE,
        related_name="post_like",
    )
    post = models.ForeignKey(
        to=PostModel,
        verbose_name="게시글",
        on_delete=models.CASCADE,
        related_name="post_like",
    )
    is_like = models.BooleanField("좋아요", default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_user_post"),
        ]
