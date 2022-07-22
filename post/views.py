from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post as PostModel
from user.serializers.signup_serializers import SignupSerializer


# url : /api/posts
class PostView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    게시글 목록 조회, 생성을 위한 view입니다.
    GET : 게시글 목록 조회
    POST : 게시글 생성
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        게시글 목록 조회

        :param request:
        :return Response: 게시글 목록 data, 상태 코드
        """

        return Response(
            SignupSerializer(PostModel.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )
