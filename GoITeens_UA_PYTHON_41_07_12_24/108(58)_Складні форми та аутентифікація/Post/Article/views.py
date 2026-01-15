from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from .models import Article, Tag
from Author.models import Author
from .forms import ArticleForm

# Create your views here.


def add_article(request: HttpRequest):
    if request.method == "POST":
        author = Author.objects.get(id=request.POST.get("author"))
        article = Article.objects.create(
            author=author,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            text=request.POST.get("text"),
        )
        tags_id = request.POST.getlist("tags")
        for tag_id in tags_id:
            tag = Tag.objects.get(id=tag_id)
            article.tags.add(tag)

        article.save()
        return redirect("index")

    context = dict(
        authors=Author.objects.all(),
        tags=Tag.objects.all()
    )
    return render(request, "add_article.html", context)


@login_required
def add_article_form(request: HttpRequest):
    if request.method == "POST":
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "add_article_form.html", dict(form=ArticleForm()))


def get_articles(request: HttpRequest):
    return render(
        request=request,
        template_name="articles.html",
        context=dict(articles=Article.objects.all())
    )
