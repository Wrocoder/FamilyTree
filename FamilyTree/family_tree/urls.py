from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('people/', views.person_list, name='person_list'),
    path('people/<int:pk>/', views.person_detail, name='person_detail'),
    ]
