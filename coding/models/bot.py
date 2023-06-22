from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from .base import AutoTimeStampedModel, HashidAutoModel

User = get_user_model()


def user_bot_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/bot/time/<filename>
    now = datetime.utcnow()
    return f"user_{instance.user_id}/bot/{now.strftime('%Y%m%d')}/{filename}"


class UserBot(HashidAutoModel, AutoTimeStampedModel):
    user = models.ForeignKey(User, related_name="bots", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    activate = models.BooleanField(default=False)
    url = models.FileField(upload_to=user_bot_path)
    win = models.PositiveIntegerField(default=0)
    draw = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "coding_userbot"
