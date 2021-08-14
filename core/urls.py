from django.urls import path
from .views import index, project, article, article_detail
urlpatterns = [
    path('', index),
    path('project', project),
    path('article', article),
    path('article/<id>', article_detail, name='article_detail')
]