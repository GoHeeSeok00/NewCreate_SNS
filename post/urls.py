from django.urls import path

from post.views import (
    PostDetailView,
    PostImageDeleteView,
    PostImageView,
    PostLikeView,
    PostUnLikeView,
    PostView,
)

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="post"),
    path("/<obj_id>", PostDetailView.as_view(), name="post_detail"),
    path("/<obj_id>/images", PostImageView.as_view(), name="post_image"),
    path("/<obj_id>/like", PostLikeView.as_view(), name="post_like"),
    path("/<obj_id>/unlike", PostUnLikeView.as_view(), name="post_unlike"),
    path("/images/<obj_id>", PostImageDeleteView.as_view(), name="post_image_delete"),
]
