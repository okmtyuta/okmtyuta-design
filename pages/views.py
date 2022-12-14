from django.shortcuts import render
from django.views.generic import TemplateView

def user_detail(request):
    template_name = "pages/user_detail.html"
    return render(request, template_name)

class GlobalDesignGuidelineView(TemplateView):
    template_name = "pages/global_design_guideline.html"

def variable(request):
    template_name = "pages/variable.html"
    return render(request, template_name)