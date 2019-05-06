
from django.urls import path, include

import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('one_article', blog.views.one_article),
    path('index', blog.views.get_index_page)
]
