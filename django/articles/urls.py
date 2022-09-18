from django.urls import path

from .views import home_view, article_view

urlpatterns = [
    path('article/<int:id>/', article_view, name='article'),
    path('', home_view)
]
