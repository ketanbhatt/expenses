from django.urls import path
from .views import AccountRegisterView, CreateAccessTokenView


urlpatterns = [
    path("register/", AccountRegisterView.as_view(), name="plaid_register"),
    path(
        "post-register/",
        CreateAccessTokenView.as_view(),
        name="plaid_create_access_token",
    ),
]
