from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'family_tree/index.html')


def about(request):
    return render(request, 'family_tree/about.html', {'title': 'About Us'})


def contact(request):
    pass


def login(request):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
