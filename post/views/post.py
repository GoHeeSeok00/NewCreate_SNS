from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import PostModel
from post.serializers import PostListSerializer, PostSerializer


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

        :param page:        페이지네이션을 위한 파라미터입니다.             default = 1
        :param limit:       페이지네이션 개수를 정하기 위한 파라미터입니다. default = 10
        :param sorting:     정렬 방법을 정하는 파라미터입니다.              default = -created_at
        :param searching:   검색을 위한 파라미터입니다.                     default = ""
        :param hashtags:    필터를 위한 파라미터입니다.                     default = ""
        :return Response:   게시글 목록 data, 상태코드
        """

        # 페이지네이션 설정
        page = int(request.GET.get("page", 1) or 1)
        limit = int(request.GET.get("limit", 10) or 10)
        offset = limit * (page - 1)

        # 정렬 설정
        sorting = request.GET.get("sorting", "-created_at") or "-created_at"

        # 검색 설정
        search = request.GET.get("searching", "") or ""
        search_list = search.split(" ")

        search_posts = PostModel.objects.filter(title__icontains=search_list[0])

        for word in search_list[1:]:
            search_posts = search_posts | PostModel.objects.filter(
                title__icontains=word
            )

        # 필터 설정
        hashtag = request.GET.get("hashtags", "") or ""
        if hashtag == "":
            pass
        else:
            hashtag_list = hashtag.split(",")

            for word in hashtag_list:
                search_posts = search_posts.filter(hashtags_text__icontains=f"#{word},")

        # 조건에 맞는 게시글 가져오기
        posts = search_posts.order_by(sorting).filter(status__status="public")[
            offset : offset + limit
        ]
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
