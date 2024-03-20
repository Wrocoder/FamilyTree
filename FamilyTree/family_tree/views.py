from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Person, FamilyRelationship


def index(request):
    return render(request, 'family_tree/index.html')


def about(request):
    return render(request, 'family_tree/about.html', {'title': 'About Us'})


def contact(request):
    pass


def login(request):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found, OOOPS...</h1>")


def person_list(request):

    people = Person.objects.all()
    return render(request, 'family_tree/person_list.html', {'people': people})
# @login_required
# def person_list(request):
#     """ View all persons """
#     user_family = request.person.family
#     people = Person.objects.filter(family=user_family)
#     return render(request, 'family_tree/person_list.html', {'people': people})


def person_detail(request, pk):
    """ Person information in details"""
    person = Person.objects.get(pk=pk)
    relationships = FamilyRelationship.objects.filter(from_person=person)
    return render(request, 'family_tree/person_detail.html', {'person': person, 'relationships': relationships})
