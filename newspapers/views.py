from django.shortcuts import render
from .models import Newspaper

def newspaper_list(request):
    template_name = "newspapers/newspaper_list.html"
    newspapers = Newspaper.objects.all().order_by("-created_at")
    picked_up_newspapers = Newspaper.objects.filter(is_picked_up=True).order_by("-created_at")

    context = {
        "newspapers": newspapers,
        "picked_up_newspapers": picked_up_newspapers,
    }
    return render(request, template_name, context)

def newspaper_detail(request, pk):
    newspaper = Newspaper.objects.get(pk = pk)
    context = {
        "newspaper": newspaper,
        "twitter_card": newspaper,
    }
    template_name = "newspapers/newspaper_detail.html"
    return render(request, template_name, context)
