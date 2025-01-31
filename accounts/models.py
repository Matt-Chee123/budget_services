from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class Providers(models.Model):
    provider_id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True,editable=False)
    provider_name = models.CharField(max_length=20)
    provider_info = models.CharField(max_length=50)
    provider_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'providers'

class Accounts(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4,primary_key=True, unique=True,editable=False)
    account_name = models.CharField(max_length=20)
    provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE)
    total = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts'