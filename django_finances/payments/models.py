from django.db import models
from django_finances.settings import Settings


class Payment(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: status, etc.

    if Settings.TRANSACTION_ENABLED:
        transaction = models.OneToOneField('transactions.Transaction', related_name='payment', on_delete=models.PROTECT)
