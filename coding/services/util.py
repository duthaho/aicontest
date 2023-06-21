import random
import string


def get_random_string(length) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))
