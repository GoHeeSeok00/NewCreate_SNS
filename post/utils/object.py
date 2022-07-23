from post.models import PostModel


def get_object_return_object_or_none(self, obj_id):
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


def get_object_and_check_permission_return_object_or_none(self, obj_id):
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
