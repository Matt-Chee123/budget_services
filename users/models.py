from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = "users_profiles"
