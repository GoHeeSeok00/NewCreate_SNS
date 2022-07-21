from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from user.models import User as UserModel
from user.serializers.signup_serializers import SignupSerializer
from user.serializers.user_serializers import UserDetailSerializer, UserListSerializer


# url : /api/users/signup
class SignupView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    회원가입을 위한 view입니다. 회원가입 기능은 POST method로 동작합니다.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = SignupSerializer

    def post(self, request):
        """
        회원가입

        :param request.data["email"]:           이메일 (중복확인)
        :param request.data["password"]:        비밀번호
        :param request.data["password_check"]:  비밀번호 확인
        :param request.data["username"]:        사용자 이름
        :param request.data["nickname"]:        닉네임 (중복확인)
        :param request.data["mobile"]:          핸드폰 번호
        :param request.data["date_of_birth"]:   생년월일

        :return Response: 메시지 and 상태 코드
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)


# url : /api/users
class UserView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.22

    사용자 목록 조회를 위한 view입니다. 조회 기능은 GET method로 동작합니다.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserListSerializer

    def get(self, request):
        """
        사용자 목록 조회

        :param request:
        :return Response: 사용자 목록, 상태 코드
        """
        user_serializer = self.serializer_class(UserModel.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)


# url : /api/users/<int:obj_id>
class UserDetailView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.22

    사용자 상세 조회, 정보 수정을 위한 view입니다.
    GET : 회원 상세 조회
    PUT : 회원 정보 수정
    """

    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 희석
        obj_id : int
        input 인자로 단일 오브젝트를 가져오고, 퍼미션 검사를 하는 메서드입니다.
        DoesNotExist 에러 발생 시 None을 리턴합니다.
        """
        try:
            object = UserModel.objects.get(id=obj_id)
        except UserModel.DoesNotExist:
            return

        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, obj_id):
        """
        사용자 상세 조회

        :param request:
        :param obj_id: 사용자 모델의 기본키(id필드)
        :return Response: (에러 or 메시지) and 상태 코드 응답
        """
        user = self.get_object_and_check_permission(obj_id)
        if not user:
            return Response(
                {"error": "존재하지 않는 회원입니다."}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(UserDetailSerializer(user).data, status=status.HTTP_200_OK)
