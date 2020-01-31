from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('conductores_sort/',
    #      views.conductores_sort.as_view(), name='conductores_sort'),
    path('conductores_list/', views.conductores),
    path('drivers/', views.ConductoresListView.as_view(), name='conductores'),
    path('drivers/add/', views.ConductoresCreate.as_view(), name='conductor_new'),
    path('drivers/<int:pk>/',
         views.ConductoresUpdate.as_view(), name='conductor_edit'),
    path('drivers/<int:pk>/borrar/',
         views.ConductoresDelete.as_view(), name='conductor_borrar'),
    path('owners/', views.ConductoresListView.as_view(), name='propietarios'),
    path('owners/add/', views.PropietariosCreate.as_view(), name='propietario_new'),
    path('owners/<int:pk>/',
         views.PropietariosUpdate.as_view(), name='propietario_edit'),
    path('owners/<int:pk>/borrar/',
         views.PropietariosDelete.as_view(), name='propietario_borrar'),
    path('cars/', views.CarrosListView.as_view(), name='carros'),
    path('cars/add/', views.CarrosCreate.as_view(), name='carros_new'),
    path('cars/<int:pk>/',
         views.CarrosUpdate.as_view(), name='carros_edit'),
    path('cars/<int:pk>/borrar/',
         views.PropietariosDelete.as_view(), name='carros_borrar'),

    path('insurance/', views.PolizasListView.as_view(), name='polizas'),
    path('insurance/add/', views.PolizaCreate.as_view(), name='poliza_new'),
    path('insurance/<int:pk>/',
         views.PolizaUpdate.as_view(), name='poliza_edit'),
    path('insurance/<int:pk>/borrar/',
         views.PolizaDelete.as_view(), name='poliza_borrar'),

    # path('conductores_sort/<str:sort>/',
    #      views.conductores_sort.as_view(), name='conductores_sort'),

    # API URL's
    path('api/conductores', views.ListaConductores.as_view()),
    path('api/carros', views.ListaCarros.as_view()),
    path('api/polizas', views.ListaPolizas.as_view()),
    path('api/propietarios', views.ListaPropietarios.as_view()),
    path('api/tipogasto', views.ListaTipoGasto.as_view()),
    path('api/renta', views.ListaRentas.as_view()),
    path('api/conductores/<int:pk>/', views.DetalleConductores.as_view()),
    path('api/carros/<int:pk>/', views.DetalleCarros.as_view()),
    path('api/polizas/<int:pk>/', views.DetallePolizas.as_view()),
    path('api/propietarios/<int:pk>/', views.DetallePropietarios.as_view()),
    path('api/tipogasto/<int:pk>/', views.DetalleTipoGasto.as_view()),
    path('api/renta/<int:pk>/', views.DetalleRentas.as_view())

]
