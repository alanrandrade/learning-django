from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('another', views.another_view, name='another_view'),
]