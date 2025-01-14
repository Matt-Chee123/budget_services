from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nationality = models.CharField(max_length=100, blank=True, null=True)

