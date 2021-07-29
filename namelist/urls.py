from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('adicionar', views.devil_name_add, name='devil_name_add'),
]

urlpatterns += [
    path('nomes', views.DevilNameList.as_view(), name='devil_name_list'),
    path('nome/<int:pk>', views.DevilNameDetail.as_view(), name='devil_name_detail'),
    path('nome/adicionar/', views.DevilNameCreate.as_view(), name='devil_name_create'),
    path('nome/<int:pk>/editar/', views.DevilNameUpdate.as_view(), name='devil_name_update'),
    path('nome/<int:pk>/remover/', views.DevilNameDelete.as_view(), name='devil_name_delete'),
]