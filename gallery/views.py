from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Illust, IllustComment
from .forms import IllustSearchForm, IllustCommentCreateForm

def illust_list(request):
    template_name = "gallery/illust_list.html"

    form = IllustSearchForm(request.GET or None)
    illusts = Illust.objects.all().order_by("-created_at")
    if form.is_valid():
        tags = form.cleaned_data.get('tags')
        if tags:
            for tag in tags:
                illusts = Illust.objects.filter(illust_tags = tag)
        
        key_word = form.cleaned_data.get('key_word')
        if key_word:
            for word in key_word.split():
                illusts = Illust.objects.filter(Q(title__icontains=word) | Q(body__icontains=word) | Q(caption__icontains=word))

    picked_up_illusts = Illust.objects.filter(is_picked_up=True).order_by("-created_at")

    context = {
        "illusts": illusts,
        "picked_up_illusts": picked_up_illusts,
        "illust_search_form": form
    }
    return render(request, template_name, context)

def illust_detail(request, pk):
    template_name = "gallery/illust_detail.html"
    illust = Illust.objects.get(pk = pk)
    comments = IllustComment.objects.filter(target=illust)
    print(comments)
    context = {
        "illust": illust,
        "comments": comments,
        # "twitter_card": article,
    }
    return render(request, template_name, context)


def illust_comment_create(request, pk):
    template_name = "gallery/illust_comment_form.html"

    if request.method == "GET":
        form = IllustCommentCreateForm(request.GET or None)

    if request.method == "POST":
        illust = get_object_or_404(Illust, pk=pk)

        form = IllustCommentCreateForm(request.POST)
        comment = form.save(commit=False)
        comment.target = illust
        comment.save()
        print(form)

        return redirect("gallery:illust_detail", pk=pk)
    
    context = {
        "form": form,
        "illust": get_object_or_404(Illust, pk=pk)
    }

    return render(request, template_name, context)