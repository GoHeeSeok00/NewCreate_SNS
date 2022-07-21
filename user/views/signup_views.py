from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.signup_serializers import UserSignupSerializer


# url : /api/users/signup
class SignupView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    회원가입을 위한 view입니다. 회원가입 기능은 post method로 동작합니다.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSignupSerializer

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

        :return Response: 메시지 and 상태 코드 응답
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
