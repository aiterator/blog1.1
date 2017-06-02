from django.shortcuts import render

# Create your views here.
from blog.models import *
def Index(request):
    articles = Article.objects.order_by('-time')
    return render(request, 'index.html', {'title':'aiterator', 'articles': articles})