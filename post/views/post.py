from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostListSerializer, PostSerializer
from post.services.post_service import (
    get_post_filtering_result,
    get_post_paging_result,
    get_post_searching_result,
    get_post_sorting_result,
)


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

        :param page:        현재 페이지                                  default = 1
        :param limit:       한 페이지의 게시글 수                        default = 10
        :param sorting:     정렬 조건                                    default = -created_at
        :param searching:   검색어(" "를 기준으로 split)                 default = ""
        :param hashtags:    필터를 위한 해시 태그(","를 기준으로 split)  default = ""
        :param post-status: 게시글 status                                default = "public"
        :return Response:   게시글 목록 data, http status
        """

        # 검색
        search = request.GET.get("searching", "") or ""
        search_list = search.split(" ")
        posts = get_post_searching_result(search_list)

        # 필터
        hashtag = request.GET.get("hashtags", "") or ""
        if hashtag != "":
            hashtag_list = hashtag.split(",")
            posts = get_post_filtering_result(posts, hashtag_list)

        # status
        post_status = request.GET.get("post-status", "public") or "public"

        # 게시글 status가 list에 없는 경우
        if post_status not in ["public", "private", "delete"]:
            return Response(
                {
                    "error": "post의 status는 'public', 'private', 'delete' 중 하나만 선택 가능합니다."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # status가 public인 게시글을 조회한다면 전체조회
        if post_status == "public":
            posts = posts.filter(status__status=post_status)
        # status가 private or delete 일때는 내가 작성한 글만 조회
        else:
            posts = posts.filter(user=request.user, status__status=post_status)

        # 정렬
        sorting = request.GET.get("sorting", "-created_at") or "-created_at"
        posts = get_post_sorting_result(posts, sorting)

        # 페이지네이션
        page = int(request.GET.get("page", 1) or 1)
        limit = int(request.GET.get("limit", 10) or 10)
        posts = get_post_paging_result(posts, page, limit)

        return Response(
            PostListSerializer(posts, many=True).data, status=status.HTTP_200_OK
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
