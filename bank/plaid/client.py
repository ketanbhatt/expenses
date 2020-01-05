import plaid
from django.conf import settings

client = plaid.Client(
    client_id=settings.PLAID_CLIENT_ID,
    secret=settings.PLAID_SECRET,
    public_key=settings.PLAID_PUBLIC_KEY,
    environment=settings.PLAID_ENV,
    api_version=settings.PLAID_API_VERSION,
)
