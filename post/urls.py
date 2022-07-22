from django.urls import path

from post.views import PostView

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="post"),
]
