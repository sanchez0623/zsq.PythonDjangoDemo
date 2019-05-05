from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article

# Create your views here.


def hello_world(request):
    return HttpResponse("hello world")


def one_article(request):
    article = Article.objects.all()[0]
    return HttpResponse('title: %s, brief: %s, content: %s,id: %s, publish_date: %s' % (article.title, article.brief, article.content, article.id, article.publish_date))
