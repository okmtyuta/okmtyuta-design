from django.shortcuts import render
from .models import UpdateInfo

# Create your views here.
def top(request):
    template_name = "top/top.html"
    update_infos = UpdateInfo.objects.all().order_by("-created_at")
    context = {
        "update_infos": update_infos
    }
    return render(request, template_name, context)