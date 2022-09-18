# from django.shortcuts import render
from django.http import HttpResponse, Http404

def home_view(request):
    return HttpResponse('Это главная страница со список последних статей.')

def article_view(request, id):
    return HttpResponse(f'Это страница статьи с id={id}')
