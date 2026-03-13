from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.filter(is_published=True).select_related('category').order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})
