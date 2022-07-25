from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostLikeSerializer
from post.utils import get_post_object_return_object_or_none


# /api/posts/<obj_id>/like
class PostLikeView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요를 위한 view입니다.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, obj_id):
        """
        :param obj_id:       게시글 오브젝트 아이디
        :return Response:    (게시글 데이터 or 에러) and 상태코드

        request.data에 user, post 정보를 담아 시리얼라이저를 요청합니다.
        """

        # 게시글 유효성 검사
        post = get_post_object_return_object_or_none(self, obj_id)
        if not post:
            return Response(
                {"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        request.data["user"] = request.user.id
        request.data["post"] = obj_id

        serializer = PostLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "좋아요 성공"}, status=status.HTTP_201_CREATED)


# /api/posts/<obj_id>/unlike
class PostUnLikeView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요 취소를 위한 view입니다.
    """

    def post(self, request, obj_id):
        """

        :param request:
        :param obj_id:
        :return:
        """
        return Response()
