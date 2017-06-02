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
class Comment(models.Model):
    #评论
    blog = models.ForeignKey(Article, verbose_name='博客')
    name = models.CharField('呢称', max_length=16)
    email = models.EmailField('邮箱')
    time = models.DateTimeField('发布时间', auto_now_add=True)
    content = models.CharField('内容', max_length=500)

    def __str__(self):
        return self.name

class About(models.Model):
    #关于
    content = models.TextField(u'内容')
    def __str__(self):
        return self.content




