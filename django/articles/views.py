from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Article

def home_view(request):
    # Ищем все статьи со статусом 2 (Опубликовано) и сортируем по дате создания.
    articles = Article.objects.filter(status=2).order_by('created_at')
    return render(request, 'home.html', {'articles': articles})

def article_view(request, id):
    # Ищем статью по id со статусом 2 (Опубликовано).
    article = get_object_or_404(Article, pk=id, status=2)

    # Эту строку раскомментить, когда будет готов шаблон.
    # return render(request, 'article_template.html', {'article': article})
    # А эту удалить:
    return HttpResponse(f'''<h1>{article.title}</h1>{article.text}''')
