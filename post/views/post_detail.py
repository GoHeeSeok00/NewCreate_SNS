from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from post.serializers import PostDetailGetSerializer
from post.utils import add_view_count, get_object_return_object_or_none


# url : /api/posts/<obj_id>
class PostDetailView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 상세 조회, 게시글 수정, 게시글 상태 변경을 위한 view입니다.
    GET : 게시글 상세 조회
    PUT : 게시글 수정
    PATCH : 게시글 상태 변경
    permission : method는 로그인 한 유저 접근가능, object는 작성자만 접근 가능
    """

    permission_classes = [IsOwner]

    def get(self, request, obj_id):
        """
        게시글 상세 조회

        :param obj_id: 게시글 오브젝트 아이디
        :return Response:
        """
        add_view_count(self, obj_id)  # 조회수 1증가
        post = get_object_return_object_or_none(self, obj_id)
        if not post:
            return Response(
                {"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(PostDetailGetSerializer(post).data, status=status.HTTP_200_OK)
