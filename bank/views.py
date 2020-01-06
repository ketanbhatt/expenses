from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import permissions

from bank.models import BankAccount
from bank.plaid import plaid_client


class AccountRegisterView(LoginRequiredMixin, TemplateView):
    template_name = "plaid/link.html"
    extra_context = {
        "plaid_country_codes": settings.PLAID_COUNTRY_CODES,
        "plaid_env": settings.PLAID_ENV,
        "plaid_public_key": settings.PLAID_PUBLIC_KEY,
        "plaid_products": settings.PLAID_PRODUCTS,
    }


class CreateAccessTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        public_token = request.data["public_token"]

        exchange_response = plaid_client.Item.public_token.exchange(public_token)
        access_token = exchange_response["access_token"]

        BankAccount.update_or_create_access_token(request.user, access_token)

        return HttpResponse()
