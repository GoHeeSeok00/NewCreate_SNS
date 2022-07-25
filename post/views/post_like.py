from rest_framework.response import Response
from rest_framework.views import APIView


class PostLikeView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.25

    게시글 좋아요를 위한 view입니다.
    """

    def post(self, request, obj_id):
        """

        :param request:
        :param obj_id:
        :return:
        """
        return Response()


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
