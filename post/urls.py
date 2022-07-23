from django.urls import path

from post.views import PostDetailView, PostImageDeleteView, PostImageView, PostView

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="post"),
    path("/<obj_id>", PostDetailView.as_view(), name="post_detail"),
    path("/<obj_id>/images", PostImageView.as_view(), name="post_image"),
    path("/images/<obj_id>", PostImageDeleteView.as_view(), name="post_image_delete"),
]
