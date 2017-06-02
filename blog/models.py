# coding=utf-8
from django.db import models
from django import forms

class Tag(models.Model):
    #标签
    tag = models.CharField(u'标签', max_length=50)
    def __str__(self):
        return self.tag

class Catagory(models.Model):
    #归档
    cat = models.CharField(u'归属', max_length=50)
    def __str__(self):
        return self.cat

class Article(models.Model):
    #博文
    title = models.CharField(u'标题', max_length=50)
    cat = models.ForeignKey(Catagory, verbose_name=u'归档')
    tag = models.ManyToManyField(Tag, verbose_name=u'标签')
    time = models.DateTimeField(u'时间', auto_now_add=True)
    visited = models.IntegerField(u'访问次数', default=0)
    content = models.TextField(u'正文')
    def __str__(self):
        return self.title

class FriendsLink(models.Model):
    #友链
    content = models.TextField(u'内容')
    def __str__(self):
        return self.content

class Comment(forms.Form):
    #评论
    name = forms.CharField(label='呢称', max_length=16, error_messages={
        'requied': '请填写呢称',
        'max_length': '呢称太长'
    })

    email = forms.EmailField(label='邮箱',error_messages={
        'requied': '请填写邮箱',
        'invalid': '邮箱格式不正确'
    })

    content = forms.CharField(label='评论内容', max_length=500, error_messages={
        'requied': '请填写评论内容!',
        'max_length': '评论内容过长'
    })
    def __str__(self):
        return self.name

class About(models.Model):
    #关于
    content = models.TextField(u'内容')
    def __str__(self):
        return self.content




