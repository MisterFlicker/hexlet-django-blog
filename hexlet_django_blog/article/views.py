from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = 'Name of app is article'
    return render(
        request,
        'articles/article.html',
        context={'name': name},
    )
