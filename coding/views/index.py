from typing import Any, Dict

from coding.services.util import get_random_string, id_to_hash
from coding.views.base import BaseView


class IndexView(BaseView):
    template_name = "coding/index.html"
