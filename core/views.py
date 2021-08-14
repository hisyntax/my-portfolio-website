from typing import AbstractSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Article, Project, Picture, Cv, About
from .forms import CommentForm

def index(request):
    projects = Project.objects.order_by('-timestamp')[:10]
    cv = Cv.objects.all()
    picture = Picture.objects.all()
    about = About.objects.all()
    context = {
        'project': projects,
        'cv': cv,
        'picture': picture,
        'about': about,
    }
    return render(request, 'index.html', context)

def project(request):
    projects = Project.objects.all().order_by('-timestamp')
    paginator = Paginator(projects, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'project.html', context)

def article(request):
    article = Article.objects.all().order_by('-timestamp')

    paginator = Paginator(article, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'article.html', context)

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'article-detail.html', context)
