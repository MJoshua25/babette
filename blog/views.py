from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData


# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    data = {
        'article': models.Article.objects.filter(status=True).order_by('-date_add')[:6]
    }
    return render(request, 'pages/blog/blog-carousel.html', mergeData(request, data))


def single_blog(request: HttpRequest, titre_slug: str) -> HttpResponse:
    if request.method == 'POST':
        article_id = request.POST.get('article')
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        cover = request.FILES['cover']
        c = models.Commentaire(
            article_id=int(article_id),
            prenom=prenom,
            nom=nom,
            email=email,
            message=message,
            cover=cover
        )
        c.save()
        return redirect('blog:index')
    else:

        data = {
            'categories': models.Categorie.objects.filter(status=True).order_by('-date_add')[:6],
            'articles': models.Article.objects.filter(status=True).order_by('-date_add')[:2],
            'single': models.Article.objects.filter(titre_slug=titre_slug)[:1].get(),
        }

        return render(request, 'pages/blog/blog-single-post.html', mergeData(request, data))
