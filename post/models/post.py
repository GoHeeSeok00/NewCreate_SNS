from django.db import models

from config.models import TimeStamp as TimeStampModel
from user.models import User as UserModel


class Status(models.Model):
    status = models.CharField("상태", max_length=20)


class Post(TimeStampModel):
    """
    Assignee : 고희석
    Date : 2022.07.22

    TimeStamp 모델을 상속받는 게시글 테이블입니다.
    TimeStamp 필드 : created_at, updated_at deleted_at
    """

    user = models.ForeignKey(
        to=UserModel, verbose_name="사용자", on_delete=models.CASCADE, related_name="post"
    )
    status = models.ForeignKey(
        to=Status, verbose_name="상태", on_delete=models.CASCADE, related_name="post"
    )

    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")
    hashtags_text = models.TextField("해시태그")
    view_count = models.IntegerField("조회수", default=0)
    like_count = models.IntegerField("좋아요수", default=0)

    def __str__(self):
        return f"제목 : {self.title} / 작성자 : {self.user.nickname}"
