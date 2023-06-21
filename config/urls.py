from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from coding.views.account import SignUpView, ActivateAccount

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("activate/<uidb64>/<token>/", ActivateAccount.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),
    path("", include("coding.urls")),
]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
