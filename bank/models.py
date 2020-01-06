from django.contrib.auth import get_user_model
from django.db import models

from common.models import TimeStampMixin


class BankAccount(TimeStampMixin, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=128, null=True, blank=True)

    @classmethod
    def update_or_create_access_token(cls, user, access_token):
        account, is_created = BankAccount.objects.update_or_create(
            user=user, defaults={"access_token": access_token}
        )
        return account, is_created
