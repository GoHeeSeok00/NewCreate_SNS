from post.models import PostModel


def get_post_searching_result(words):
    """
    Assignee : 고희석
    Date : 2022.08.27

    게시글 검색 결과를 반환합니다.

    :param words: 검색 단어 리스트
    :return: PostModel 쿼리셋
    """

    results = PostModel.objects.filter(title__icontains=words[0])
    for word in words[1:]:
        results = results | PostModel.objects.filter(title__icontains=word)
    return results


def get_post_filtering_result(posts, words):
    """
    Assignee : 고희석
    Date : 2022.08.27

    게시글 필터 결과를 반환합니다.

    :param posts: PostModel 쿼리셋
    :param words: 필터 단어 리스트
    :return: PostModel 쿼리셋
    """

    for word in words:
        posts = posts.filter(hashtags_text__icontains=f"#{word},")
    return posts


def get_post_sorting_result(posts, sorting):
    """
    Assignee : 고희석
    Date : 2022.08.27

    게시글 정렬 결과를 반환합니다.

    :param posts: PostModel 쿼리셋
    :param sorting: 정렬 조건
    :return: PostModel 쿼리셋
    """

    return posts.order_by(sorting)


def get_post_paging_result(posts, page, limit):
    """
    Assignee : 고희석
    Date : 2022.08.27

    게시글 페이지네이션 결과를 반환합니다.

    :param posts: PostModel 쿼리셋
    :param page: 현재 페이지
    :param limit: 한 페이지의 게시글 수
    :return: PostModel 쿼리셋
    """

    offset = limit * (page - 1)
    return posts[offset : offset + limit]
