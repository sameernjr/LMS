from django.urls import path
from . import views

urlpatterns = [
    path('layout/', views.index, name='index'),
]
