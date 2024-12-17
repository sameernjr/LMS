from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fullsail/', views.fullsail, name='fullsail'),
    path('coloradostate/', views.coloradostate, name='coloradostate'),
    path('oregonstate/', views.oregonstate, name='oregonstate'),
    path('saintlouis/', views.saintlouis, name='saintlouis'),
]
