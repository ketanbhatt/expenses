from django.urls import path, include
from .views import TransactionViewSet

from rest_framework import routers

transaction_router = routers.DefaultRouter()
transaction_router.register("v1", TransactionViewSet)

urlpatterns = [
    path("api/", include(transaction_router.urls)),
]
