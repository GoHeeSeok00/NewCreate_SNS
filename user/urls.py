from django.urls import path

from user.views.signup_views import SignupView

app_name = "user"

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
]
