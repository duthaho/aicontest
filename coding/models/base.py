from django.db import models
from hashid_field import HashidAutoField


class HashidAutoModel(models.Model):
    id = HashidAutoField(primary_key=True)

    class Meta:
        abstract = True


class AutoTimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
