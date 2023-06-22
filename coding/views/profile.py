import math

from django import forms
from django.http import QueryDict
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from coding.const import DEFAULT_PAGE_SIZE
from coding.models.bot import UserBot
from coding.models.profile import UserProfile
from coding.services.util import safe_int
from coding.views.base import BaseView


class UserBotForm(forms.ModelForm):
    class Meta:
        model = UserBot
        fields = (
            "name",
            "activate",
            "url",
        )


class ProfileView(BaseView):
    template_name = "coding/profile.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        total, page, bot_list = 1, 1, []
        profile = UserProfile.objects.filter(pk=kwargs.get("profile_hash")).first()
        if profile:
            bot_count = UserBot.objects.filter(user_id=profile.user_id).count()
            total = math.ceil(bot_count / DEFAULT_PAGE_SIZE) or 1
            page = safe_int(self.request.GET.get("page")) or 1
            if page > total:
                page = total
            offset = (page - 1) * DEFAULT_PAGE_SIZE
            bot_list = UserBot.objects.filter(user_id=profile.user_id).order_by(
                "-activate", "-id"
            )[offset : offset + DEFAULT_PAGE_SIZE]
        data.update(
            total=total,
            page=page,
            bot_list=bot_list,
            profile=profile,
            me=self.request.user.profile.id == kwargs.get("profile_hash"),
        )
        return data

    def get(self, request, *args, **kwargs):
        form = UserBotForm()
        context = self.get_context_data(**kwargs)
        if not context.get("profile"):
            raise Http404()
        return render(request, self.template_name, dict(form=form, **context))

    def post(self, request, *args, **kwargs):
        form = UserBotForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get("activate"):
                UserBot.objects.filter(user=request.user).update(activate=False)
            UserBot.objects.create(user=request.user, **form.cleaned_data)
            return HttpResponseRedirect(reverse("profile", kwargs=kwargs))
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, dict(form=form, **context))

    def delete(self, request, *args, **kwargs):
        data = QueryDict(request.body)
        bot_id = data.get("bot_id")
        bot = UserBot.objects.filter(pk=bot_id).first()
        if not bot or bot.user_id != request.user.id:
            raise Http404()
        bot.delete()
        return JsonResponse(dict(sucess=True))
