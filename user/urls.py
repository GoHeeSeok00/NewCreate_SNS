from django.urls import path

from user.views import SignupView, UserView

app_name = "user"

urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("/signup", SignupView.as_view(), name="signup"),
]
