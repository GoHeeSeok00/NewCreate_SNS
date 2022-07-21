from django.contrib.auth import authenticate
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# url : /accounts/login
class LoginView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    로그인을 위한 view입니다. 로그인 기능은 POST method로 동작합니다.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        로그인

        :param request:
        :return Response: (에러 or 메시지, 토큰) and 상태 코드 응답
        """
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response(
                {"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # jwt token
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        return Response(
            {
                "message": "로그인 성공",
                "token": {"access": access_token, "refresh": refresh_token},
            },
            status=status.HTTP_200_OK,
        )


# url : /accounts/logout
class LogoutView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    로그아웃을 위한 view입니다. 로그아웃 기능은 POST method로 동작합니다.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        로그아웃

        :param request:
        :return Response: 메시지 and 상태 코드 응답
        """
        return Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)
