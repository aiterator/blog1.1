from django.shortcuts import render,get_object_or_404

# Create your views here.
from blog.models import *
from blog.forms import CommentForm

def Index(request):
    articles = Article.objects.order_by('-time')
    return render(request, 'index.html', {'title':'aiterator', 'articles': articles})

def Get_detail(request, id):

    article = get_object_or_404(Article, pk=id)

    if(request.method == 'GET'):
        article.visited += 1
        article.save()
    else:
        form = CommentForm(request.POST)
        if(form.is_valid()):
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = article
            Comment.objects.create(**cleaned_data)

    comments = article.comment_set.all().order_by('-time')
    return render(request, 'get_detail.html', {
        'title': article.title,
        "article": article,
        'comments': comments,
        'form': CommentForm(),
    })

def About_me(request):
    content = About.objects.first().content
    return render(request, 'about_me.html',{'title': '关于', 'content': content})

def Friend_link(request):
    links = FriendsLink.objects.first()
    return render(request, 'friend_link.html', {'title': '友链', 'links': links})

def Get_all_tags(request):
    tags_all = Tag.objects.all()
    tags_all_detail = {}
    for s in tags_all:
        tags_all_detail[s] = s.article_set.all().order_by('-time')
    return render(request, 'get_all_tags.html', {
        'title': 'tags',
        'how_many': tags_all.count(),
        'tags_all_detail': tags_all_detail,
    })

