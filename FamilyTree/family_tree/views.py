from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [
    {'title': 'About Us', 'url_name': 'about'},
    {'title': 'Contact Us', 'url_name': 'contact'},

]


def index(request):
    data = {'title': 'Family Tree',
            'menu': menu
            }
    return render(request, 'family_tree/index.html', context=data)


def about(request):
    return render(request, 'family_tree/about.html', {'title': 'About Us', 'menu': menu})


def contact(request):
    pass


def login(request):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
