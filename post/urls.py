from django.urls import path

from post.views import PostDetailView, PostImageView, PostView

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="post"),
    path("/<obj_id>", PostDetailView.as_view(), name="post_detail"),
    path("/<obj_id>/images", PostImageView.as_view(), name="post_image"),
]
