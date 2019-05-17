from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article

# Create your views here.


def hello_world(request):
    return HttpResponse("hello world")


def one_article(request):
    article = Article.objects.all()[0]
    return HttpResponse('title: %s, brief: %s, content: %s,id: %s, publish_date: %s' % (article.title, article.brief, article.content, article.id, article.publish_date))


def get_index_page(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'article_list': articles})


# def get_detail_page(request):
#     current_article = Article.objects.all()[0]
#     section_article=current_article.content.split('\n')
#     return render(request, 'blog/detail.html', {'current_article': current_article,'section_article':section_article})

# 获取某一个id的文章
def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    current_article = None
    for article in all_article:
        if article.id == article_id:
            current_article = article
            break

    section_article = current_article.content.split('\n')
    return render(request, 'blog/detail.html', {'current_article': current_article, 'section_article': section_article})
