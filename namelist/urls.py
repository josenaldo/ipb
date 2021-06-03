from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lista-completa', views.DevilNameListView, name='listacompleta'),
]