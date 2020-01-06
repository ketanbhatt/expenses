from rest_framework import permissions

from common.rest_framework.permissions import IsOwnerEditingObject
from common.rest_framework.viewsets import ModelViewSetNoDestroy
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSetNoDestroy):
    permission_classes = [permissions.IsAuthenticated, IsOwnerEditingObject]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.filter(is_soft_deleted=False)

    def get_queryset(self):
        qs = super(TransactionViewSet, self).get_queryset()
        return qs.filter(user=self.request.user)
