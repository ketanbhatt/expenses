from django.urls import path
from .views import register, exchange_for_access_token


urlpatterns = [
    path("register/", register, name="plaid_register"),
    path(
        "exchange/", exchange_for_access_token, name="plaid_exchange_for_access_token"
    ),
]
