from django.db import models


class TimeStamp(models.Model):
    """
    Assignee : 희석
    Date : 2022.07.22

    created_at, updated_at, deleted_at(DateTimeField) 필드를
    사용하는 모델을 위한 기본 모델입니다.
    abstract = True 설정으로 물리적인 테이블이 생성되지 않습니다.
    """

    created_at = models.DateTimeField("작성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)
    deleted_at = models.DateTimeField("삭제시간", default=None, null=True, blank=True)

    class Meta:
        abstract = True
