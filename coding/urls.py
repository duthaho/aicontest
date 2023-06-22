from django.urls import path, re_path

from .views.index import IndexView
from .views.profile import ProfileView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    re_path(
        r"^profile/(?P<profile_hash>[a-zA-Z0-9]+)/$",
        ProfileView.as_view(),
        name="profile",
    ),
]
