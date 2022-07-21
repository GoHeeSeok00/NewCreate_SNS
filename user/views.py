from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from user.serializers.signup_serializers import SignupSerializer
from user.serializers.user_serializers import UserListSerializer


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
