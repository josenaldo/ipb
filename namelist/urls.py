from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nomes', views.DevilNameListView.as_view(), name='devil_name_list'),
    path('nome/<int:pk>', views.DevilNameDetailView.as_view(), name='devil_name_detail'),
]