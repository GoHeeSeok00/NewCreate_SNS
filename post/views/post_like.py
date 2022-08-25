from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostLikeSerializer, PostUnLikeSerializer
from post.utils import (
    get_post_like_object_return_object_or_none,
    get_post_object_return_object_or_none,
)


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
        :return Response:    (메세지 or 에러) and 상태코드

        request.data에 user, post 정보를 담아 시리얼라이저를 요청합니다.
        """

        # 게시글 유효성 검사
        post = get_post_object_return_object_or_none(self, obj_id)
        if not post:
            return Response(
                {"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        # 좋아요 유효성 검사
        request.data["user"] = request.user.id
        request.data["post"] = obj_id

        # 좋아요 모델 유효성 검사
        post_like = get_post_like_object_return_object_or_none(self, **request.data)
        if not post_like:
            serializer = PostLikeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "좋아요 성공"}, status=status.HTTP_200_OK)

        request.data["is_like"] = True

        serializer = PostLikeSerializer(post_like, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "좋아요 성공"}, status=status.HTTP_200_OK)


# /api/posts/<obj_id>/unlike
class PostUnLikeView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요 취소를 위한 view입니다.
    """

    def post(self, request, obj_id):
        """

        :param obj_id:       게시글 좋아요 객체 아이디
        :return Response:    (메세지 or 에러) and 상태코드

        request.data에 user, post 정보를 담아 시리얼라이저를 요청합니다.
        """

        request.data["user"] = request.user.id
        request.data["post"] = obj_id

        post_like = get_post_like_object_return_object_or_none(self, **request.data)
        if not post_like:
            return Response(
                {"error": "좋아요 기록이 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        request.data["is_like"] = False

        serializer = PostUnLikeSerializer(post_like, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "좋아요 취소 성공"}, status=status.HTTP_200_OK)
