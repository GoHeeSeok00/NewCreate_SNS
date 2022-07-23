from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from post.serializers import PostImageSerializer


# url : /api/posts/<obj_id>/images
class PostImageView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.23

    게시글 사진 등록, 삭제를 위한 view입니다.
    POST : 게시글 사진 등록
    DELETE : 게시글 사진 삭제
    permission : method는 로그인 한 유저 접근가능, object는 작성자만 접근 가능
    """

    permission_classes = [IsOwner]

    def post(self, request, obj_id):
        """
        게시글 이미지 등록

        :param obj_id: 게시글 오브젝트 아이디
        :param request["image"]: 게시글 사진
        :return:
        """
        serializer = PostImageSerializer(data=request.data, context={"post": obj_id})
        serializer.is_valid(raise_exception=True)
        image_instance = serializer.save()
        return Response(
            {"message": "이미지 등록 성공", "image": image_instance.image.url},
            status=status.HTTP_201_CREATED,
        )
