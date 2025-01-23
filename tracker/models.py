from tkinter.constants import CASCADE
from django.db import models
from users.models import UserProfile
import uuid

# Create your models here.
class Income(models.Model):
    income_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    income_name = models.CharField(max_length=40)
    time_frame = models.CharField(max_length=10)
    income_type = models.CharField(max_length=10)
    income_amount = models.IntegerField()
    user = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,null=False)

    class Meta:
        db_table = 'user_income'