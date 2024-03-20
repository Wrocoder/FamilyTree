from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'family_tree/index.html', {'title': 'Family Tree'})



@login_required
def about(request):
    return render(request, 'family_tree/about.html', {'title': 'About Us'})


@login_required
def contact(request):
    return render(request, 'family_tree/contact.html', {'title': 'Contact Us'})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
