from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('people/', views.person_list, name='person_list'),
    path('people/<int:pk>/', views.person_detail, name='person_detail'),
    path('new_family_member/', views.new_family_member, name='new_family_member'),
    ]
