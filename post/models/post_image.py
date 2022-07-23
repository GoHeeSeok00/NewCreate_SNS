from django.db import models

from post.models.post import Post as PostModel


class PostImage(models.Model):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 사진을 저장하는 테이블입니다.
    """

    post = models.ForeignKey(
        to=PostModel,
        verbose_name="게시글",
        on_delete=models.CASCADE,
        related_name="post_image",
    )
    image = models.ImageField(
        "게시글 사진", upload_to="post/static/post_image/", max_length=None
    )
