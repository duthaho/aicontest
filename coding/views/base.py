from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from coding.services.util import id_to_hash


class BaseView(LoginRequiredMixin, generic.TemplateView):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        avatar = f"https://www.gravatar.com/avatar/{self.request.user.profile.id}?s=32&d=identicon&r=PG"
        data.update(avatar=avatar)
        return data
