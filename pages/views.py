from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UpdateInfo


def top(request):
    template_name = "pages/top.html"
    update_infos = UpdateInfo.objects.all().order_by("-created_at")
    context = {
        "update_infos": update_infos
    }
    return render(request, template_name, context)


def user_detail(request):
    template_name = "pages/user_detail.html"
    return render(request, template_name)


class DesignPolicy(TemplateView):
    template_name = "pages/design_policy.html"


def variable(request):
    template_name = "pages/variable.html"
    return render(request, template_name)