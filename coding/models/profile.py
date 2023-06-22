from django.contrib.auth import get_user_model
from django.db import models

from .base import HashidAutoModel

User = get_user_model()


class UserProfile(HashidAutoModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # win = models.PositiveIntegerField(default=0)
    # draw = models.PositiveIntegerField(default=0)
    # lose = models.PositiveIntegerField(default=0)
    # point = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "coding_userprofile"
