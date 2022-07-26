from django.core.exceptions import PermissionDenied

from post.models import PostImageModel, PostLikeModel, PostModel


def get_post_object_return_object_or_none(self, obj_id):
    """
    Assignee : 희석
    Date : 2022.07.23

    :param obj_id: 게시글 객체 아이디
    :return: object or none

    obj_id로 객체를 가져옵니다.
    게시글 상태가 public이거나 장성자와 요청자가 일치하면 object를 리턴합니다.
    DoesNotExist 에러 발생 시 None을 리턴합니다.
    """
    try:
        object = PostModel.objects.get(id=obj_id)

        if object.status.status != "public":  # public이 아닌경우
            if object.user != self.request.user:  # 작성자가 요청자와 일치하지 않는경우
                return

    except PostModel.DoesNotExist:
        return
    return object


def get_post_object_and_check_permission_return_object_or_none(self, obj_id):
    """
    Assignee : 희석
    Date : 2022.07.23

    :param obj_id: 게시글 객체 아이디

    obj_id로 객체를 가져오고, 퍼미션 검사를 하는 메서드입니다.
    DoesNotExist 에러 발생 시 None을 리턴합니다.
    """
    try:
        object = PostModel.objects.get(id=obj_id)
    except PostModel.DoesNotExist:
        return

    self.check_object_permissions(self.request, object)
    return object


def get_post_image_object_and_check_permission_return_object_or_none(self, obj_id):
    """
    Assignee : 희석
    Date : 2022.07.23

    :param obj_id: 게시글 사진 객체 아이디

    obj_id로 객체를 가져오고, 퍼미션 검사를 하는 메서드입니다.
    DoesNotExist 에러 발생 시 None을 리턴합니다.
    """
    try:
        object = PostImageModel.objects.get(id=obj_id)
    except PostImageModel.DoesNotExist:
        return

    self.check_object_permissions(self.request, object)
    return object


def get_post_like_object_return_object_or_none(self, user, post):
    """
    Assignee : 희석
    Date : 2022.07.25

    :param obj_id: 게시글 사진 객체 아이디

    obj_id로 객체를 가져오고, 퍼미션 검사를 하는 메서드입니다.
    DoesNotExist 에러 발생 시 None을 리턴합니다.
    """
    try:
        object = PostLikeModel.objects.get(user_id=user, post_id=post)
    except PostLikeModel.DoesNotExist:
        return

    if self.request.user != object.user:
        raise PermissionDenied("접근 권한이 없습니다.")
    return object
