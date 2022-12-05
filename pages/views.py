from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UpdateInfo

# Create your views here.
def nostalon_top(request):
    template_name = "pages/nostalon_top.html"
    update_infos = UpdateInfo.objects.all().order_by("-created_at")
    context = {
        "update_infos": update_infos
    }
    return render(request, template_name, context)


def coming_soon(request):
    template_name = "pages/coming_soon.html"
    return render(request, template_name)

def user_detail(request):
    template_name = "pages/user_detail.html"
    return render(request, template_name)

class GlobalDesignGuidelineView(TemplateView):
    template_name = "pages/global_design_guideline.html"

def variable(request):
    template_name = "pages/variable.html"
    return render(request, template_name)