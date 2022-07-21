from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import LoginView

app_name = "account"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LoginView.as_view(), name="logout"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
]
