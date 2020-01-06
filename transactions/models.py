import datetime

from django.contrib.auth import get_user_model
from django.db import models

from common.models import TimeStampMixin


class Transaction(TimeStampMixin, models.Model):
    class CreationSource(models.TextChoices):
        MANUAL = "manual", "Created Manually"
        MANUAL_BANK_SYNC = "manual-bank-sync", "Synced from Bank manually"
        AUTOMATIC_BANK_SYNC = "auto-bank-sync", "Synced from Bank automatically"

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    transaction_date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=256)
    amount = models.FloatField()
    comments = models.TextField(null=True, blank=True)

    category = models.CharField(max_length=64)  # Change these to FKs and M2Ms later
    sub_categories = models.TextField()

    creation_source = models.CharField(
        choices=CreationSource.choices, default=CreationSource.MANUAL, max_length=32
    )
    is_approved = models.BooleanField(default=True)
    is_soft_deleted = models.BooleanField(default=False)
