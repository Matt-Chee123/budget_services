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


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    min = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    max = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)


