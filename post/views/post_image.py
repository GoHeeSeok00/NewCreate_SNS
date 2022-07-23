from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from post.serializers import PostImageSerializer
from post.utils import (
    get_post_image_object_and_check_permission_return_object_or_none,
    get_post_object_and_check_permission_return_object_or_none,
)


# url : /api/posts/<obj_id>/images
class PostImageView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 사진 등록, 삭제를 위한 view입니다.
    POST : 게시글 사진 등록
    permission : method는 로그인 한 유저 접근가능, object는 작성자만 접근 가능
    """

    permission_classes = [IsOwner]

    def post(self, request, obj_id):
        """
        게시글 이미지 등록

        :param obj_id: 게시글 오브젝트 아이디
        :param request["image"]: 게시글 사진
        :return Response: (메시지, 이미지 주소 or 에러) and 상태코드
        """
        post = get_post_object_and_check_permission_return_object_or_none(self, obj_id)
        if not post:
            return Response(
                {"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PostImageSerializer(data=request.data, context={"post": post})
        serializer.is_valid(raise_exception=True)
        image_instance = serializer.save()
        return Response(
            {"message": "이미지 등록 성공", "image": image_instance.image.url},
            status=status.HTTP_201_CREATED,
        )


# url : /api/posts/images/<obj_id>
class PostImageDeleteView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 사진 등록, 삭제를 위한 view입니다.
    POST : 게시글 사진 등록
    permission : method는 로그인 한 유저 접근가능, object는 작성자만 접근 가능
    """

    permission_classes = [IsOwner]

    def delete(self, request, obj_id):
        """
        게시글 이미지 삭제

        :param obj_id: 게시글 사진 오브젝트 아이디
        :return Response: (메시지 or 에러) and 상태코드
        """
        post_image = get_post_image_object_and_check_permission_return_object_or_none(
            self, obj_id
        )
        if not post_image:
            return Response(
                {"error": "삭제할 이미지가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        post_image.delete()
        return Response({"message": "이미지 삭제 성공"}, status=status.HTTP_200_OK)
