from django.shortcuts import render
from .models import Article

def article_list(request):
    template_name = "article/article_list.html"
    articles = Article.objects.all().order_by("-created_at")
    picked_up_articles = Article.objects.filter(is_picked_up=True).order_by("-created_at")

    context = {
        "articles": articles,
        "picked_up_articles": picked_up_articles,
    }
    return render(request, template_name, context)

def article_detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        "article": article,
        "twitter_card": article,
    }
    template_name = "article/article_detail.html"
    return render(request, template_name, context)
