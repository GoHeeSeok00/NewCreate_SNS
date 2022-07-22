from user.models import User as UserModel


def get_object_and_check_permission(self, obj_id):
    """
    Assignee : 희석
    Date : 2022.07.22

    :param obj_id: 사용자 모델의 기본키(id필드)

    인자로 오브젝트의 id를 가져오고, 퍼미션 검사를 하는 메서드입니다.
    DoesNotExist 에러 발생 시 None을 리턴합니다.
    """
    try:
        object = UserModel.objects.get(id=obj_id)
    except UserModel.DoesNotExist:
        return

    self.check_object_permissions(self.request, object)
    return object
