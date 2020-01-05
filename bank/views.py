from django.conf import settings
from django.shortcuts import render

from django.http import HttpResponse

from bank.plaid import plaid_client


def register(request):
    return render(
        request,
        "plaid/link.html",
        {
            "plaid_country_codes": settings.PLAID_COUNTRY_CODES,
            "plaid_env": settings.PLAID_ENV,
            "plaid_public_key": settings.PLAID_PUBLIC_KEY,
            "plaid_products": settings.PLAID_PRODUCTS,
        },
    )


def exchange_for_access_token(request):
    public_token = request.POST["public_token"]
    exchange_response = plaid_client.Item.public_token.exchange(public_token)

    print(exchange_response)
    return HttpResponse()
