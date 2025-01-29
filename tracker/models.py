from django.db import models
from django.conf import settings
import uuid

class Income(models.Model):
    income_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    income_name = models.CharField(max_length=40)
    time_frame = models.CharField(max_length=10)
    income_type = models.CharField(max_length=10)
    income_amount = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_income'
