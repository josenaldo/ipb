from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('invocacao', views.invocacao, name='invocacao' ),
    # path('adicionar', views.devil_name_add, name='devil_name_add'),
]

urlpatterns += [
    path('nomes/', views.DevilNameList.as_view(), name='devil_name_list'),
    path('nomes/<int:pk>', views.DevilNameDetail.as_view(), name='devil_name_detail'),
    path('nomes/adicionar/', views.DevilNameCreate.as_view(), name='devil_name_create'),
    path('nomes/<int:pk>/editar/', views.DevilNameUpdate.as_view(), name='devil_name_update'),
    path('nomes/<int:pk>/remover/', views.DevilNameDelete.as_view(), name='devil_name_delete'),
]