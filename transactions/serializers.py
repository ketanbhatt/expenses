from rest_framework import serializers

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        if self.instance is None:
            kwargs["user"] = self.context["request"].user

        return super(TransactionSerializer, self).save(**kwargs)

    class Meta:
        model = Transaction
        exclude = ["user", "created_at", "updated_at"]
