from django.urls import path

from user.views import SignupView, UserDetailView, UserView, UserWithdraw

app_name = "user"

urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("/signup", SignupView.as_view(), name="signup"),
    path("/<int:obj_id>", UserDetailView.as_view(), name="user_detail"),
    path("/<int:obj_id>/withdraw", UserWithdraw.as_view(), name="withdraw"),
]
