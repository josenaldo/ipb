from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('invocacao', views.invocacao, name='invocacao' ),
    path('forca', views.forca, name='forca'),
]

urlpatterns += [
    path('nomes/', views.DevilNameList.as_view(), name='devilname_list'),
    path('nomes/<int:pk>', views.DevilNameDetail.as_view(), name='devilname_detail'),
    path('nomes/adicionar/', views.DevilNameCreate.as_view(), name='devilname_create'),
    path('nomes/<int:pk>/editar/', views.DevilNameUpdate.as_view(), name='devilname_update'),
    path('nomes/<int:pk>/remover/', views.DevilNameDelete.as_view(), name='devilname_delete'),

    path('nomes/importar/', views.devilname_import, name='devilname_import'),
    path('api/random', views.random_name, name='random'),
]

from django.urls import include
from rest_framework import routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'devilnames', views.DevilNameViewSet)
# router.register(r'random', views.RandomDevilNameViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]