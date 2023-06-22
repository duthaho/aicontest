from contextlib import suppress
import random
import string

from django.conf import settings
from hashids import Hashids


def get_random_string(length: int) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


def id_to_hash(id: int, length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    return Hashids(settings.SECRET_KEY, min_length=length, alphabet=alphabet).encrypt(
        id
    )


def safe_int(num: any, default: int = 0) -> int:
    with suppress(Exception):
        return int(num)
    return default
