from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post as PostModel
from post.serializers import PostSerializer
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
        :return Response: 게시글 목록 data, 상태코드
        """
        return Response(
            SignupSerializer(PostModel.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        """
        게시글 생성

        :param request.data["status"]:          게시글 상태 (public, private) :int
        :param request.data["title"]:           게시글 제목 :str
        :param request.data["content"]:         게시글 내용 :str
        :param request.data["hashtags_text"]:   해시태그 ('#'으로 시작하고 ','로 끝나는 문자열) :str
        :return Response:                       에러 or 메시지, 상태코드
        """
        serializer = PostSerializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "게시글 작성 성공"}, status=status.HTTP_201_CREATED)
