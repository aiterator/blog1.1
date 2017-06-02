from django.shortcuts import render,get_object_or_404

# Create your views here.
from blog.models import *

def Index(request):
    articles = Article.objects.order_by('-time')
    return render(request, 'index.html', {'title':'aiterator', 'articles': articles})

def Get_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    article.visited += 1
    article.save()
    return render(request, 'get_detail.html', {'title': article.title, "article": article})
