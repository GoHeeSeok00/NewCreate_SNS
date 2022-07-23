from django.db.models import F

from post.models import PostModel


def add_view_count(self, obj_id):
    """
    Assignee : 희석
    Date : 2022.07.23

    :param obj_id: 게시글 객체 아이디

    obj_id로 게시글을 필터하여 조회수를 1 증가시킵니다.
    """
    PostModel.objects.filter(id=obj_id).update(view_count=F("view_count") + 1)
