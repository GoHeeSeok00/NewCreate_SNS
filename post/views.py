from rest_framework.views import APIView


# url : /api/posts
class PostView(APIView):
    """
    Assignee : 고희석
    Date : 2022.07.21

    게시글 목록 조회, 생성을 위한 view입니다.
    GET : 게시글 목록 조회
    POST : 게시글 생성
    """
